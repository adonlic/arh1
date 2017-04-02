from FRISC.assembler.messages.message_list import MessageList, Message, MessageType

from FRISC.assembler.lexic.token import Token, TokenType

from FRISC.assembler.frisc.instr_format import InstructionFormat


class FRISCParser:
    __instance = None

    def __init__(self):
        pass

    @staticmethod
    def getInstance():
        if FRISCParser.__instance is None:
            FRISCParser.__instance = FRISCParser()

        return FRISCParser.__instance

    def parse(self, tokenized_row):
        filtered_formats = list()
        token_id = 0
        base_token_id = 0
        token = None
        token_type = tokenized_row[0].getTokenType()

        if token_type == TokenType.LABEL:
            token_id += 1
        if not len(tokenized_row) == 1:
            token = tokenized_row[token_id]
        else:
            return True

        print(token)
        if token.getTokenType() in [TokenType.INSTRUCTION, TokenType.PSEUDO_INSTRUCTION]:
            # parse everything after mnemonic...
            filtered_formats = self.__filter_formats(InstructionFormat.getValidFormats(), token.getValue().upper())
            token_id += 1
            base_token_id = token_id
        else:
            # parsing has failed if first 'real thing' is not mnemonic...
            return False

        success = True

        # foreach format, check rest...
        for instr_format in filtered_formats:
            token_id = base_token_id

            # for format_token in instr_format:
            for format_token_id in range(1, len(instr_format)):
                token = tokenized_row[token_id]
                token_type = token.getTokenType()
                token_value = token.getValue()
                # token_value = token.getValue().upper()

                # if isinstance(format_token[0], list):
                #     break_again = False
                #
                #     for t in format_token[0]:
                #         if token_type in t:
                #             success = True
                #         else:
                #             success = False
                #             break_again = True
                #             break
                #
                #     if break_again:
                #         break
                # else:
                #     if token_type in format_token[0]:
                #         success = True
                #     else:
                #         # it has an error...
                #         success = False
                #         break

                # check if token type is equal to token type (all except mnemonic)
                # and check if first token   ...
                if token_type == instr_format[format_token_id]:
                    success = True
                    token_id += 1

                    if token_id == len(tokenized_row):
                        # continue
                        break

                    continue
                else:
                    # it has an error...
                    success = False
                    break

        if not success:
            return False
        else:
            return True

    def __filter_formats(self, instr_formats, mnemonic):
        temp = list()
        result = list()

        for instr in instr_formats:
            if mnemonic in instr[0]:
                temp.append(instr)
                # result.append(instr)

                instruction = list()
                put_commas = True

                # get last saved instruction and put commas in between...
                for current_token_id in range(len(temp[len(temp) - 1])):
                    current_token = temp[len(temp) - 1][current_token_id]

                    if current_token_id % 2 == 0 and current_token_id != 0 and put_commas:
                        instruction.append(TokenType.COMMA)
                        instruction.append(current_token)

                        if current_token == TokenType.LEFT_PAREN:
                            put_commas = False
                    elif current_token_id == 0 or current_token_id % 1 == 0:
                        instruction.append(current_token)

                result.append(instruction)

        return result
