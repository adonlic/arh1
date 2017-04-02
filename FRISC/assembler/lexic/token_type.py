class TokenType:
    """
    Keeps token types as public static variables, unchangeable.
    """

    PSEUDO_INSTRUCTION = 0b0000
    INSTRUCTION = 0b0001
    REGISTER = 0b0010
    STATUS_REGISTER = 0b0011
    INTERMEDIATE_VALUE = 0b0100
    INTERMEDIATE_BASE = 0b0101
    COMMA = 0b0110
    LEFT_PAREN = 0b0111
    RIGHT_PAREN = 0b1000
    PLUS = 0b1001
    MINUS = 0b1010
    CONDITION = 0b1011
    LABEL = 0b1100

    UNKNOWN = 0b1101

    @staticmethod
    def getPrintableRepr(token_type):
        """
        Returns printable representation version of token type.

        :param token_type:  Token that needs its type representation.
        :return:            String representation of given token type.
        """

        if token_type == TokenType.PSEUDO_INSTRUCTION:
            return 'PSEUDO_INSTRUCTION'
        elif token_type == TokenType.INSTRUCTION:
            return 'INSTRUCTION'
        elif token_type == TokenType.REGISTER:
            return 'REGISTER'
        elif token_type == TokenType.STATUS_REGISTER:
            return 'STATUS_REGISTER'
        elif token_type == TokenType.INTERMEDIATE_VALUE:
            return 'INTERMEDIATE_VALUE'
        elif token_type == TokenType.INTERMEDIATE_BASE:
            return 'INTERMEDIATE_BASE'
        elif token_type == TokenType.COMMA:
            return 'COMMA'
        elif token_type == TokenType.LEFT_PAREN:
            return 'LEFT_PAREN'
        elif token_type == TokenType.RIGHT_PAREN:
            return 'RIGHT_PAREN'
        elif token_type == TokenType.PLUS:
            return 'PLUS'
        elif token_type == TokenType.MINUS:
            return 'MINUS'
        elif token_type == TokenType.CONDITION:
            return 'CONDITION'
        elif token_type == TokenType.LABEL:
            return 'LABEL'
        elif token_type == TokenType.UNKNOWN:
            return 'UNKNOWN'

    @staticmethod
    def getTabCorrection(token_type):
        """
        Returns tab correction for each type so printing can look nicer.
        Types that require less letters to be represented also require more tabs.

        :param token_type:  Token type.
        :return:            Number of tabs depending on token type.
        """

        if token_type == TokenType.PSEUDO_INSTRUCTION:
            return '\t'
        elif token_type == TokenType.INSTRUCTION:
            return '\t\t\t'
        elif token_type == TokenType.REGISTER:
            return '\t\t\t'
        elif token_type == TokenType.STATUS_REGISTER:
            return '\t\t'
        elif token_type == TokenType.INTERMEDIATE_VALUE:
            return '\t'
        elif token_type == TokenType.INTERMEDIATE_BASE:
            return '\t'
        elif token_type == TokenType.COMMA:
            return '\t\t\t\t'
        elif token_type == TokenType.LEFT_PAREN:
            return '\t\t\t'
        elif token_type == TokenType.RIGHT_PAREN:
            return '\t\t\t'
        elif token_type == TokenType.PLUS:
            return '\t\t\t\t'
        elif token_type == TokenType.MINUS:
            return '\t\t\t\t'
        elif token_type == TokenType.CONDITION:
            return '\t\t\t'
        elif token_type == TokenType.LABEL:
            return '\t\t\t\t'
        elif token_type == TokenType.UNKNOWN:
            return '\t\t\t'
