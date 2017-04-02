class Register:
    R0 = 'R0'
    R1 = 'R1'
    R2 = 'R2'
    R3 = 'R3'
    R4 = 'R4'
    R5 = 'R5'
    R6 = 'R6'
    R7 = 'R7'
    SR = 'SR'

    @staticmethod
    def all():
        return [Register.R0, Register.R1, Register.R2, Register.R3,
                Register.R4, Register.R5, Register.R6, Register.R7,
                Register.SR]

    @staticmethod
    def all_R():
        return [Register.R0, Register.R1, Register.R2, Register.R3,
                Register.R4, Register.R5, Register.R6, Register.R7]

    @staticmethod
    def all_special():
        return [Register.SR]
