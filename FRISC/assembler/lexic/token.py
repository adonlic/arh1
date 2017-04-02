from FRISC.assembler.lexic.token_type import TokenType


class Token:
    """
    Keeps token's basic information such as:
        - type
        - value
        - line (row number in source file)
        - start (column number in source file)
    """

    def __init__(self, token_type: TokenType, value: str, line: int, start: int):
        """
        Initializes token (supplies it with basic information).

        :param token_type:  Token type of current token (TokenType object).
        :param value:       Token's value (pattern from source file).
        :param line:        Line number (row number) where token was detected.
        :param start:       Column number of token.
        """

        self.__token_type = token_type
        self.__value = value
        self.__line = line
        self.__start = start

    def getTokenType(self):
        """
        Returns token type of current token.

        :return:    Token type (TokenType object).
        """

        return self.__token_type

    def getValue(self):
        """
        Returns token's value (pattern from source file).

        :return:    Token value (string).
        """

        return self.__value

    def getLine(self):
        """
        Returns row number where token was taken.

        :return:    Row number (integer).
        """

        return self.__line

    def setLine(self, line):
        """
        Sets new line of current token.

        :param line:    New row number.
        :return:        Nothing.
        """

        self.__line = line

    def getStart(self):
        """
        Returns column number on which token begins in source file.

        :return:    Column number (integer).
        """

        return self.__start

    def getPrintableRepr(self):
        """
        Returns printable representation version of current token.
        Format:
            TOKEN_TYPE  line    start   value

        :return:
        """

        token_type_repr = TokenType.getPrintableRepr(self.__token_type)
        # correction is required if we want good alignment of elements after type repr...
        correction = TokenType.getTabCorrection(self.__token_type)

        return token_type_repr + correction + str(self.__line) + '\t\t' + str(self.__start) + '\t\t' + self.__value
