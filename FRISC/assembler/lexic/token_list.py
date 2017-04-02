from FRISC.assembler.lexic.token import Token, TokenType


class TokenList:
    """
    Keeps all data about tokens in given row and has option to supply and
    modify data. For example, when label must be removed and instead of it put
    intermediate address value.
    """

    def __init__(self, line: int):
        """
        Initializes list of tokens and saves line number where this tokens are.

        :param line:    Row number from source file.
        """

        self.__tokens = list()
        self.__line = line

        self.__next_id = -1

    def __iter__(self):
        """
        When this object is called in for loop, this method's called.

        :return:
        """

        return self

    def __next__(self):
        """
        Gives 'next' token item when for loop is iterating.

        :return:    Token object at corresponding position.
        """

        self.__next_id += 1

        if self.__next_id == len(self.__tokens):
            raise StopIteration

        return self.__tokens[self.__next_id]

    def __len__(self):
        """
        Returns number of how many tokens is in current row.

        :return:    Number of tokens in the list.
        """

        return len(self.__tokens)

    def __getitem__(self, item):
        """
        Returns token by given index (item).

        :param item:    Index, position of item in list.
        :return:        Token if found, None if not found.
        """

        if len(self.__tokens) > item:
            return self.__tokens[item]

        return None

    def getTokens(self):
        """
        Returns list of tokens.

        :return:    List of tokens (consists of Token objects).
        """

        return self.__tokens

    def getTokensPrintableRepr(self):
        """
        Gives report of tokens in given row (row number is tied to TokenList
        object.

        :return:    Representation of all token's information in some row.
        """

        output = 'line_{}\n'.format(self.__line)
        output += '------------------------------------------\n'

        for token in self.__tokens:
            output += token.getPrintableRepr() + '\n'

        return output

    def getLine(self):
        """
        Returns row number from source file where token was detected.

        :return:    Row number in source file
        """

        return self.__line

    def setLine(self, line: int):
        """
        Changes line number. This situation is possible when some instructions
        must be reordered or just moved upside down.

        :param line:    New line number where all this tokens will be.
        :return:        Nothing
        """

        self.__line = line

        for token in self.__tokens:
            token.setLine(line)

    def append(self, token: Token):
        """
        Adds new token in current source code row.

        :param token:   Token to be added.
        :return:        Nothing.
        """

        self.__tokens.append(token)

    def remove(self, position: int):
        """
        Maybe some tokens we won't need, like pseudo instructions later.
        They'll be erased when CPU instructions are modified properly.

        :param position:    Position of token in the row.
        :return:            Nothing
        """

        self.__tokens.remove(position)

    def change_token(self, new_token: Token):
        """
        This method has only one purpose: to find label and change it for intermediate
        value that's supposed to go there.

        :param new_token:   Token that should have intermediate value.
        :return:            Nothing
        """

        for pos in range(len(self.__tokens)):
            # if label is found, exchange it for memory location of the label or exchange
            # value from register for register's name
            if self.__tokens[pos] == TokenType.LABEL:
                self.__tokens[pos] = new_token
                break
