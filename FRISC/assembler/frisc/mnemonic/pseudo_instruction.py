class PseudoInstruction:
    ORG = 'ORG'
    EQU = 'EQU'
    DW = 'DW'
    DH = 'DH'
    DB = 'DB'
    DS = 'DS'
    MACRO = 'MACRO'
    ENDMACRO = 'ENDMACRO'

    @staticmethod
    def all():
        return [PseudoInstruction.ORG, PseudoInstruction.EQU, PseudoInstruction.DW, PseudoInstruction.DH,
                PseudoInstruction.DB, PseudoInstruction.DS, PseudoInstruction.MACRO, PseudoInstruction.ENDMACRO]
