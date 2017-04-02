class Instruction:
    MOVE = 'MOVE'
    OR = 'OR'
    AND = 'AND'
    XOR = 'XOR'
    ADD = 'ADD'
    ADC = 'ADC'
    SUB = 'SUB'
    SBC = 'SBC'
    ROTL = 'ROTL'
    ROTR = 'ROTR'
    SHL = 'SHL'
    SHR = 'SHR'
    ASHR = 'ASHR'
    CMP = 'CMP'
    POP = 'POP'
    PUSH = 'PUSH'
    LOADB = 'LOADB'
    STOREB = 'STOREB'
    LOADH = 'LOADH'
    STOREH = 'STOREH'
    LOAD = 'LOAD'
    STORE = 'STORE'
    JP = 'JP'
    JR = 'JR'
    CALL = 'CALL'
    RET = 'RET'
    RETI = 'RETI'
    RETN = 'RETN'
    HALT = 'HALT'

    @staticmethod
    def all():
        return [Instruction.MOVE, Instruction.OR, Instruction.AND, Instruction.XOR,
                Instruction.ADD, Instruction.ADC, Instruction.SUB, Instruction.SBC,
                Instruction.ROTL, Instruction.ROTR, Instruction.SHL, Instruction.SHR,
                Instruction.ASHR, Instruction.CMP, Instruction.POP, Instruction.PUSH,
                Instruction.LOADB, Instruction.STOREB, Instruction.LOADH, Instruction.STOREH,
                Instruction.LOAD, Instruction.STORE, Instruction.JP, Instruction.JR,
                Instruction.CALL, Instruction.RET, Instruction.RETI, Instruction.RETN,
                Instruction.HALT]
