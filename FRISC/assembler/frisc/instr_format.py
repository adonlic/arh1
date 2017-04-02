from FRISC.assembler.lexic.token_type import TokenType

from FRISC.assembler.frisc.mnemonic.instruction import Instruction
from FRISC.assembler.frisc.mnemonic.pseudo_instruction import PseudoInstruction
from FRISC.assembler.frisc.mnemonic.register import Register


class InstructionFormat:
    @staticmethod
    def getValidFormats():
        formats = list()

        # REGISTER INSTRUCTIONS
        formats.append('move|r|r')
        formats.append('move|i|r')
        formats.append('move|r|sr')
        formats.append('move|i|sr')
        formats.append('move|sr|r')

        # ALU INSTRUCTIONS
        formats.append('or|r|r|r')
        formats.append('and|r|r|r')
        formats.append('xor|r|r|r')
        formats.append('add|r|r|r')
        formats.append('adc|r|r|r')
        formats.append('sub|r|r|r')
        formats.append('sbc|r|r|r')
        formats.append('rotl|r|r|r')
        formats.append('rotr|r|r|r')
        formats.append('shl|r|r|r')
        formats.append('shr|r|r|r')
        formats.append('ashr|r|r|r')
        formats.append('cmp|r|r|r')
        # intermediate
        formats.append('or|r|i|r')
        formats.append('and|r|i|r')
        formats.append('xor|r|i|r')
        formats.append('add|r|i|r')
        formats.append('adc|r|i|r')
        formats.append('sub|r|i|r')
        formats.append('sbc|r|i|r')
        formats.append('rotl|r|i|r')
        formats.append('rotr|r|i|r')
        formats.append('shl|r|i|r')
        formats.append('shr|r|i|r')
        formats.append('ashr|r|i|r')
        formats.append('cmp|r|i|r')

        # MEMORY INSTRUCTIONS
        formats.append('pop|r')
        formats.append('push|r')
        formats.append('load{b, h}|r|i')
        formats.append('store{b, h}|r|i')
        formats.append('load{b, h}|r|(|r|+|i|)')
        formats.append('store{b, h}|r|(|r|+|i|)')

        new = InstructionFormat.__putCommas(formats)
        a = 2

        # register instructions
        formats.append([Instruction.MOVE, TokenType.REGISTER, TokenType.REGISTER])
        formats.append([Instruction.MOVE, TokenType.INTERMEDIATE_VALUE, TokenType.REGISTER])
        formats.append([Instruction.MOVE, TokenType.REGISTER, TokenType.STATUS_REGISTER])
        formats.append([Instruction.MOVE, TokenType.INTERMEDIATE_VALUE, TokenType.STATUS_REGISTER])
        formats.append([Instruction.MOVE, TokenType.STATUS_REGISTER, TokenType.REGISTER])

        # arithmetical logical instructions
        # function = 0
        formats.append([Instruction.OR, TokenType.REGISTER, TokenType.REGISTER, TokenType.REGISTER])
        formats.append([Instruction.AND, TokenType.REGISTER, TokenType.REGISTER, TokenType.REGISTER])
        formats.append([Instruction.XOR, TokenType.REGISTER, TokenType.REGISTER, TokenType.REGISTER])
        formats.append([Instruction.ADD, TokenType.REGISTER, TokenType.REGISTER, TokenType.REGISTER])
        formats.append([Instruction.ADC, TokenType.REGISTER, TokenType.REGISTER, TokenType.REGISTER])
        formats.append([Instruction.SUB, TokenType.REGISTER, TokenType.REGISTER, TokenType.REGISTER])
        formats.append([Instruction.SBC, TokenType.REGISTER, TokenType.REGISTER, TokenType.REGISTER])
        formats.append([Instruction.ROTL, TokenType.REGISTER, TokenType.REGISTER, TokenType.REGISTER])
        formats.append([Instruction.ROTR, TokenType.REGISTER, TokenType.REGISTER, TokenType.REGISTER])
        formats.append([Instruction.SHL, TokenType.REGISTER, TokenType.REGISTER, TokenType.REGISTER])
        formats.append([Instruction.SHR, TokenType.REGISTER, TokenType.REGISTER, TokenType.REGISTER])
        formats.append([Instruction.ASHR, TokenType.REGISTER, TokenType.REGISTER, TokenType.REGISTER])
        formats.append([Instruction.CMP, TokenType.REGISTER, TokenType.REGISTER, TokenType.REGISTER])
        # function = 1
        formats.append([Instruction.OR, TokenType.REGISTER, TokenType.INTERMEDIATE_VALUE, TokenType.REGISTER])
        formats.append([Instruction.ADD, TokenType.REGISTER, TokenType.INTERMEDIATE_VALUE, TokenType.REGISTER])
        formats.append([Instruction.ADC, TokenType.REGISTER, TokenType.INTERMEDIATE_VALUE, TokenType.REGISTER])
        formats.append([Instruction.SUB, TokenType.REGISTER, TokenType.INTERMEDIATE_VALUE, TokenType.REGISTER])
        formats.append([Instruction.SBC, TokenType.REGISTER, TokenType.INTERMEDIATE_VALUE, TokenType.REGISTER])
        formats.append([Instruction.ROTL, TokenType.REGISTER, TokenType.INTERMEDIATE_VALUE, TokenType.REGISTER])
        formats.append([Instruction.ROTR, TokenType.REGISTER, TokenType.INTERMEDIATE_VALUE, TokenType.REGISTER])
        formats.append([Instruction.SHL, TokenType.REGISTER, TokenType.INTERMEDIATE_VALUE, TokenType.REGISTER])
        formats.append([Instruction.SHR, TokenType.REGISTER, TokenType.INTERMEDIATE_VALUE, TokenType.REGISTER])
        formats.append([Instruction.ASHR, TokenType.REGISTER, TokenType.INTERMEDIATE_VALUE, TokenType.REGISTER])
        formats.append([Instruction.CMP, TokenType.REGISTER, TokenType.INTERMEDIATE_VALUE, TokenType.REGISTER])

        # memory instructions
        formats.append([Instruction.POP, TokenType.REGISTER])
        formats.append([Instruction.PUSH, TokenType.REGISTER])
        # function = 0
        formats.append([Instruction.LOADB, TokenType.REGISTER,
                        TokenType.LEFT_PAREN, TokenType.INTERMEDIATE_VALUE, TokenType.RIGHT_PAREN])
        formats.append([Instruction.STOREB, TokenType.REGISTER,
                        TokenType.LEFT_PAREN, TokenType.INTERMEDIATE_VALUE, TokenType.RIGHT_PAREN])
        formats.append([Instruction.LOADH, TokenType.REGISTER,
                        TokenType.LEFT_PAREN, TokenType.INTERMEDIATE_VALUE, TokenType.RIGHT_PAREN])
        formats.append([Instruction.STOREH, TokenType.REGISTER,
                        TokenType.LEFT_PAREN, TokenType.INTERMEDIATE_VALUE, TokenType.RIGHT_PAREN])
        formats.append([Instruction.LOAD, TokenType.REGISTER,
                        TokenType.LEFT_PAREN, TokenType.INTERMEDIATE_VALUE, TokenType.RIGHT_PAREN])
        formats.append([Instruction.STORE, TokenType.REGISTER,
                        TokenType.LEFT_PAREN, TokenType.INTERMEDIATE_VALUE, TokenType.RIGHT_PAREN])
        # function = 1
        # offset not set
        formats.append([Instruction.LOADB, TokenType.REGISTER,
                        TokenType.LEFT_PAREN, TokenType.REGISTER, TokenType.RIGHT_PAREN])
        formats.append([Instruction.STOREB, TokenType.REGISTER,
                        TokenType.LEFT_PAREN, TokenType.REGISTER, TokenType.RIGHT_PAREN])
        formats.append([Instruction.LOADH, TokenType.REGISTER,
                        TokenType.LEFT_PAREN, TokenType.REGISTER, TokenType.RIGHT_PAREN])
        formats.append([Instruction.STOREH, TokenType.REGISTER,
                        TokenType.LEFT_PAREN, TokenType.REGISTER, TokenType.RIGHT_PAREN])
        formats.append([Instruction.LOAD, TokenType.REGISTER,
                        TokenType.LEFT_PAREN, TokenType.REGISTER, TokenType.RIGHT_PAREN])
        formats.append([Instruction.STORE, TokenType.REGISTER,
                        TokenType.LEFT_PAREN, TokenType.REGISTER, TokenType.RIGHT_PAREN])
        # with + offset
        formats.append([Instruction.LOADB, TokenType.REGISTER,
                        TokenType.LEFT_PAREN, TokenType.REGISTER, TokenType.PLUS,
                        TokenType.INTERMEDIATE_VALUE, TokenType.RIGHT_PAREN])
        formats.append([Instruction.STOREB, TokenType.REGISTER,
                        TokenType.LEFT_PAREN, TokenType.REGISTER, TokenType.PLUS,
                        TokenType.INTERMEDIATE_VALUE, TokenType.RIGHT_PAREN])
        formats.append([Instruction.LOADH, TokenType.REGISTER,
                        TokenType.LEFT_PAREN, TokenType.REGISTER, TokenType.PLUS,
                        TokenType.INTERMEDIATE_VALUE, TokenType.RIGHT_PAREN])
        formats.append([Instruction.STOREH, TokenType.REGISTER,
                        TokenType.LEFT_PAREN, TokenType.REGISTER, TokenType.PLUS,
                        TokenType.INTERMEDIATE_VALUE, TokenType.RIGHT_PAREN])
        formats.append([Instruction.LOAD, TokenType.REGISTER,
                        TokenType.LEFT_PAREN, TokenType.REGISTER, TokenType.PLUS,
                        TokenType.INTERMEDIATE_VALUE, TokenType.RIGHT_PAREN])
        formats.append([Instruction.STORE, TokenType.REGISTER,
                        TokenType.LEFT_PAREN, TokenType.REGISTER, TokenType.PLUS,
                        TokenType.INTERMEDIATE_VALUE, TokenType.RIGHT_PAREN])
        # with - offset
        formats.append([Instruction.LOADB, TokenType.REGISTER,
                        TokenType.LEFT_PAREN, TokenType.REGISTER, TokenType.MINUS,
                        TokenType.INTERMEDIATE_VALUE, TokenType.RIGHT_PAREN])
        formats.append([Instruction.STOREB, TokenType.REGISTER,
                        TokenType.LEFT_PAREN, TokenType.REGISTER, TokenType.MINUS,
                        TokenType.INTERMEDIATE_VALUE, TokenType.RIGHT_PAREN])
        formats.append([Instruction.LOADH, TokenType.REGISTER,
                        TokenType.LEFT_PAREN, TokenType.REGISTER, TokenType.MINUS,
                        TokenType.INTERMEDIATE_VALUE, TokenType.RIGHT_PAREN])
        formats.append([Instruction.STOREH, TokenType.REGISTER,
                        TokenType.LEFT_PAREN, TokenType.REGISTER, TokenType.MINUS,
                        TokenType.INTERMEDIATE_VALUE, TokenType.RIGHT_PAREN])
        formats.append([Instruction.LOAD, TokenType.REGISTER,
                        TokenType.LEFT_PAREN, TokenType.REGISTER, TokenType.MINUS,
                        TokenType.INTERMEDIATE_VALUE, TokenType.RIGHT_PAREN])
        formats.append([Instruction.STORE, TokenType.REGISTER,
                        TokenType.LEFT_PAREN, TokenType.REGISTER, TokenType.MINUS,
                        TokenType.INTERMEDIATE_VALUE, TokenType.RIGHT_PAREN])

        # control instructions
        # without condition
        formats.append([Instruction.JP, TokenType.INTERMEDIATE_VALUE])
        formats.append([Instruction.JP, TokenType.REGISTER,
                        TokenType.LEFT_PAREN, TokenType.REGISTER, TokenType.PLUS,
                        TokenType.INTERMEDIATE_VALUE, TokenType.RIGHT_PAREN])
        formats.append([Instruction.JR, TokenType.REGISTER,
                        TokenType.LEFT_PAREN, TokenType.REGISTER, TokenType.PLUS,
                        TokenType.INTERMEDIATE_VALUE, TokenType.RIGHT_PAREN])
        formats.append([Instruction.CALL, TokenType.REGISTER,
                        TokenType.LEFT_PAREN, TokenType.REGISTER, TokenType.PLUS,
                        TokenType.INTERMEDIATE_VALUE, TokenType.RIGHT_PAREN])
        formats.append([Instruction.CALL, TokenType.REGISTER,
                        TokenType.LEFT_PAREN, TokenType.REGISTER, TokenType.PLUS,
                        TokenType.INTERMEDIATE_VALUE, TokenType.RIGHT_PAREN])
        formats.append([Instruction.RET, TokenType.REGISTER,
                        TokenType.LEFT_PAREN, TokenType.REGISTER, TokenType.PLUS,
                        TokenType.INTERMEDIATE_VALUE, TokenType.RIGHT_PAREN])


        return formats

    @staticmethod
    def __putCommas(formats: list):
        new_formats = list()

        for f in formats:
            tokens = f.split('|')
            new_format = list()
            new_format.append(tokens[0])    # append mnemonic
            no_more_commas = False

            if len(tokens) > 1:
                new_format.append(tokens[1])

                if len(tokens) > 2:
                    for token_id in range(2, len(tokens)):
                        if tokens[token_id] == '(':
                            no_more_commas = True
                        if no_more_commas:
                            new_format.append(tokens[token_id])
                            continue

                        new_format.append(',')
                        new_format.append(tokens[token_id])

            new_formats.append(new_format)

        return new_formats

    @staticmethod
    def getToken(format_symbol: str):
        format_symbol = format_symbol.upper()

        if format_symbol in Instruction.all():
            return TokenType.INSTRUCTION
        elif format_symbol in PseudoInstruction.all():
            return TokenType.PSEUDO_INSTRUCTION
        elif format_symbol in Register.all_R():
            return TokenType.REGISTER
        elif format_symbol in Register.all_special():
            return TokenType.STATUS_REGISTER
