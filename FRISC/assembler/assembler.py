from FRISC.assembler.lexic.tokenizer import FRISCTokenizer
from FRISC.assembler.syntax.parser import FRISCParser
from FRISC.assembler.messages.message_list import MessageList, Message, MessageType


class FRISCAssembler:
    __instance = None

    def __init__(self):
        self.__assembly = list()
        self.__machine_code = list()

        self.__messages = MessageList()
        self.__error_occurred = False
        self.__lex_report = ''  # lexical analysis result
        self.__stx_report = ''  # syntax analysis result

        self.__labels = dict()

    @staticmethod
    def getInstance():
        if FRISCAssembler.__instance is None:
            FRISCAssembler.__instance = FRISCAssembler()

        return FRISCAssembler.__instance

    def getAssembly(self):
        return self.__assembly

    def getMachineCode(self):
        return self.__machine_code

    def getMessages(self):
        return self.__messages

    def getLexicalAnalysisReport(self):
        return self.__lex_report

    def getSyntaxAnalysisReport(self):
        return self.__stx_report

    def getReport(self):
        output = ''

        output += self.__messages.getErrorsPrintableRepr()
        # output += self.__messages.getWarningsPrintableRepr()
        # output += self.__messages.getInfo()

        return output

    def assemble(self, input_rows):
        # builder = FRISCInstruction.Builder.\
        #     getInstance().\
        #     generate_machine_code('ADD', instr_param.InstructionParamKey.SRC1.value='r6',
        #                                                                       instr_param.InstructionParamKey.SRC2.value='r7',
        #                                   instr_param.InstructionParamKey.DEST.value='r7')

        # builder = FRISCInstruction.Builder. \
        #     getInstance(). \
        #     generate_machine_code('ADD', src1='r6', src2='r7', dest='r7', is_intermediate=False)

        # tokenizer = FRISCTokenizer.getInstance()    # lexical analyzer
        # parser = FRISCParser.getInstance()          # syntax analyzer

        # tokenizer.tokenize(input_rows)

        # if tokenizer.getMessages().errors_occurred():
        #     # print(tokenizer.getMessages().getErrors())
        #     print(tokenizer.getMessages().getErrorsPrintableRepr())
        tokenizer = FRISCTokenizer.getInstance()
        self.__lexical_analysis(tokenizer, input_rows)

        if self.__error_occurred:
            return False

        if not self.__syntax_analysis(tokenizer.getTokens()):
            print('zapeo')

        return True

    def __lexical_analysis(self, tokenizer, input_rows):
        tokenizer.tokenize(input_rows)

        # share messages from syntax analysis with assembler (self)...
        for message in tokenizer.getMessages():
            self.__messages.append(message)

        if tokenizer.getMessages().errors_occurred():
            self.__error_occurred = True
        else:
            self.__lex_report = tokenizer.getReport()

    def __syntax_analysis(self, token_list):
        parser = FRISCParser.getInstance()

        for token_row in token_list:
            if not parser.parse(token_row):
                return False

        return True

    def first_pass(self, input_rows):
        for row in input_rows:
            if row in self.__labels.keys():
                pass
        pass

    def second_pass(self):
        pass

    def __generate_info(self):
        pass
