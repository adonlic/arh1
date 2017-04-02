import re

from FRISC.assembler.messages.message_list import MessageList, Message, MessageType
from FRISC.assembler.messages.error_type import ErrorType

from FRISC.assembler.frisc.mnemonic.command_instr_condition import CommandInstructionCondition
from FRISC.assembler.frisc.mnemonic.instruction import Instruction
from FRISC.assembler.frisc.mnemonic.pseudo_instruction import PseudoInstruction
from FRISC.assembler.frisc.mnemonic.register import Register
from FRISC.assembler.frisc.mnemonic.intermediate_base import IntermediateBase

from FRISC.assembler.lexic.token_list import TokenList, Token, TokenType


class FRISCTokenizer:
    """
    Lexical analyzer of FRISC processor.
    Some rules:
        - source code is not case sensitive, but labels are, with "infinite" length
        - that being said, labels like 'LaBeL' and 'Label' are not same
        - comments start with ';' sign and it's required, lack of that character
            will result analyzer to fail if comment text is started without putting
            ';' character first
        - analyzer will have errors if it has detected "unknown" character outside of
            comment section (errors must be checked if they exist after analysis)
    """

    __instance = None
    __separators = [' ', '\n', '\t']
    __assembly_related_separators = [',', '(', ')', '+', '-', '_']

    def __init__(self):
        """
        Initializes token list (list of token lists) and empty message list (MessageList
        object) which keeps errors, warnings and info related to tokenizer.
        """

        self.__tokens = list()
        self.__messages = MessageList()

    @staticmethod
    def getInstance():
        """
        Tokenizer class is designed to be unique. It means, it's singleton which in
        other word means that this method creates this class's object if it doesn't
        exist (if it's not called previously). If it exists, it returns already
        made instance.

        :return:    Instance of this class on class level for uniqueness.
        """

        if FRISCTokenizer.__instance is None:
            FRISCTokenizer.__instance = FRISCTokenizer()

        return FRISCTokenizer.__instance

    def getReport(self):
        """
        Builds and returns report on whole source code basis.
        At top off it is set description for each data column.

        :return:    Report of lexical analysis
        """

        output = 'TOKEN_TYPE\t\t\tLINE\tCOLUMN\tTOKEN\n\n'

        for row_tokens in self.__tokens:
            output += row_tokens.getTokensPrintableRepr() + '\n'

        return output

    def getTokens(self):
        """
        Returns tokens (list of lists).

        :return:    Token list with each element as TokenList() object, which is
                    unique type of list.
        """

        return self.__tokens

    def getMessages(self):
        """
        Returns messages (MessageList object)

        :return:    Messages grouped in errors, warnings and info.
        """

        return self.__messages

    def tokenize(self, input_rows: list):
        """
        Iterates through source code file and builds tokens for each row.

        :param input_rows:  List of rows from source code file.
        :return:            Nothing.
        """

        line = 1

        for i in range(len(input_rows)):
            # adding new line at last row because last token will be missed if there's no new line...
            if i + 1 == len(input_rows):
                input_rows[i] += '\n'

            self.__tokenize_line(input_rows[i], line)
            line += 1

    def __tokenize_line(self, row: str, line: int):
        """
        Separates source code line by usual and FRISC related separators and tokens.

        :param row:     Row in source code file.
        :param line:    Line number in source code file.
        :return:        Nothing.
        """

        start = 1
        current_column = 1
        pattern = ''
        token_list = TokenList(line)

        for char in row:
            # INVALID CHARACTER OR COMMENT DETECTION
            if not self.__is_valid_character(char):
                # if unsupported character is used outside of comment boundary -> error
                # (sign ';' is valid, but if some weird character is used before comment section
                # then whatever it is, it's not valid)
                message = Message(MessageType.ERROR, line, start,
                                  ErrorType.UNSUPPORTED_CHARACTER, char, self)
                self.__messages.append(message)
                break
            elif char == ';':
                # if current char where comment begins, ignore it and ignore everything after it
                break

            # TOKEN DETECTION
            # there are some special characters within FRISC assembly that require special care:
            #   -   if current character is blank space and pattern exists -> analyze that pattern
            #   -   if current character is FRISC related additional problems can occur:
            #           -   if pattern is some control instruction like JP and we met '_' which
            #               means it should be condition that's supposed to come yet, we mustn't
            #               split it as character for itself because it expects condition like
            #               '_EQ' instead of 'eq' just because '_' was lost (sure, we could simplify
            #               it, but it's logical to print pattern that was found in a file and
            #               corresponding meaning, for example: if user typed JP_EQ, it shouldn't
            #               show tokenized result as JP and EQ, but instead JP is instruction, _EQ
            #               is condition)...
            #           -   all additional problems are cause of previous condition that '_' shouldn't
            #               be ignored when found after control instruction and they are handled properly
            if char in FRISCTokenizer.__separators and pattern != '':
                self.__evaluate(token_list, pattern, line, start)
                pattern = ''
            elif char in FRISCTokenizer.__assembly_related_separators:
                if self.__is_instruction(pattern):
                    # if it's some control instruction, save it and
                    # set current char (char '_') as first char in a pattern
                    self.__evaluate(token_list, pattern, line, start)
                    pattern = char
                    current_column += 1
                    continue
                elif char != '_':
                    # if it's not special underscore character, but for example comma sign...
                    # possible situation:
                    #   -   user typed ADD r0, r1, r0 and current char is ',', condition expecting
                    # blank space didn't catch pattern, but pattern must be analyzed same as current char
                    #   -   user typed ADD r0, r1 , r0 you can see there's blank space before second
                    # comma -> this all means we must check if there was pattern before...
                    # if pattern not in ['', ' ']:
                    if pattern != '':
                        self.__evaluate(token_list, pattern, line, start)
                        pattern = ''
                        start = current_column
                    self.__evaluate(token_list, char, line, start)
                    current_column += 1
                    continue
                pattern += char
            else:
                if char != ' ':
                    if pattern == '':
                        start = current_column

                    pattern += char

            current_column += 1

        if len(token_list) > 0:
            self.__tokens.append(token_list)

    def __evaluate(self, token_list: TokenList, pattern: str, line: int, start: int):
        """
        Evaluates given pattern by giving meaning to it (token).

        :param token_list   Reference on token list that keeps current row's information.
        :param pattern:     Pattern that is evaluated.
        :param line:        Line in source code file.
        :param start:       Column number in source code file.
        :return:            Nothing.
        """

        original = pattern
        pattern = pattern.upper()
        token_type = TokenType.UNKNOWN

        # check all with upper representation because pattern is set to upper
        # (assembly that'll be analyzed is not case sensitive)
        if self.__is_pseudo_instruction(pattern):
            token_type = TokenType.PSEUDO_INSTRUCTION
        elif self.__is_instruction(pattern):
            token_type = TokenType.INSTRUCTION
        elif self.__is_register(pattern):
            token_type = TokenType.REGISTER
        elif self.__is_status_register(pattern):
            token_type = TokenType.STATUS_REGISTER
        elif self.__is_intermediate(pattern):
            token_type = TokenType.INTERMEDIATE_VALUE
        elif self.__is_intermediate_base(pattern):
            token_type = TokenType.INTERMEDIATE_BASE
        elif pattern == ',':
            token_type = TokenType.COMMA
        elif pattern == '(':
            token_type = TokenType.LEFT_PAREN
        elif pattern == ')':
            token_type = TokenType.RIGHT_PAREN
        elif pattern == '+':
            token_type = TokenType.PLUS
        elif pattern == '-':
            token_type = TokenType.MINUS
        elif self.__is_condition(pattern):
            token_type = TokenType.CONDITION
        elif self.__is_label(pattern):
            token_type = TokenType.LABEL

        token = Token(token_type, original, line, start)
        token_list.append(token)

    def __is_valid_character(self, char: chr):
        """
        Validates character that's written in the file, but in comment section everything is
        allowed.

        :param char:    Character that needs to be validated.
        :return:        True or false, depending on validation result.
        """

        if re.fullmatch('([a-z]|[A-Z]|_|[0-9]|%|,|\(|\)|\+|-|;|\n|\t)', char) or char == ' ':
            return True

        return False

    def __is_pseudo_instruction(self, pattern: str):
        """
        Seeks pattern in FRISC pseudo instructions that's written in the file.
        This type of instruction is what assembler reads, not FRISC CPU.

        :param pattern:     Pattern that's questioned.
        :return:            True if it's pseudo instruction, false if it's not.
        """

        if pattern in PseudoInstruction.all():
            return True

        return False

    def __is_instruction(self, pattern: str):
        """
        Seeks pattern in FRISC instructions that's written in the file.

        :param pattern:     Pattern that's questioned.
        :return:            True if it's instruction, false if it's not.
        """

        if pattern in Instruction.all():
            return True

        return False

    def __is_register(self, pattern: str):
        """
        Seeks pattern in FRISC register file that's written in the file.

        :param pattern:     Pattern that's questioned.
        :return:            True if that kind of register exist, false if it's not.
        """

        if pattern in Register.all_R():
            return True

        return False

    def __is_status_register(self, pattern: str):
        """
        Seeks pattern in FRISC special registers (in this case it's only SR register
        in instruction commands).

        :param pattern:     Pattern that's questioned.
        :return:            True if that kind of register exist, false if it's not.
        """

        if pattern in Register.all_special():
            return True

        return False

    def __is_intermediate(self, pattern: str):
        """
        Checks if all characters of pattern are digits (bits 19-0 in FRISC instructions
        of that kind).
        It does not check if it's in proper range (semantic analyzer checks if it is).

        :param pattern:     Pattern that's questioned.
        :return:            True if all characters are digits, false if they're not.
        """

        for char in pattern:
            if not re.match('[0-9]', char):
                return False

        return True

    def __is_intermediate_base(self, pattern: str):
        """
        Checks if given pattern is explicit declaration of intermediate value, in FRISC
        syntax.

        :param pattern:     Pattern that's questioned.
        :return:            True if it's valid declaration, false if it's not.
        """

        if pattern in IntermediateBase.all():
            return True

        return False

    def __is_condition(self, pattern: str):
        """
        Seeks pattern in FRISC control instruction set of conditions.

        :param pattern:     Pattern that's questioned.
        :return:            True if it's condition, false if it's not.
        """

        if pattern in CommandInstructionCondition.all():
            return True

        return False

    def __is_label(self, pattern: str):
        """
        Checks if given pattern is label.
        Valid examples:
            - 435352
            - LabElExamPLe
            - LaBeL9435
            - LBL_check
            - MA_93
        From examples we can see that it accepts all numbers, all text, text with
        number behind it, text with underscore then text or a number.

        :param pattern: Pattern that's given on inspection.
        :return:        Returns TRUE or FALSE depending on matching result.
        """

        if re.fullmatch('([a-z]|[A-Z]|_|[0-9])+', pattern):
            return True

        return False
