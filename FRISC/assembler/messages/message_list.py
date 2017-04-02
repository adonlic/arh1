from FRISC.assembler.messages.message import Message, MessageType


class MessageList:
    """
    Keeps messages at one place with 3 types:
        - errors
        - warnings
        - info
    All three types are unique. When printed, errors and tags are shown with tag
    for each of them because some of them have information about line and column
    for specific request. It's set in that way because each error and warning is
    unique and that information is important to be at top next to tag ERROR or
    WARNING tag. As bonus, they come coloured by default :).
    """

    def __init__(self):
        """
        Initializes message list that keeps all three types of messages (errors,
        warnings and info).
        """

        self.__messages = list()
        self.__errors_count = 0
        self.__warnings_count = 0

        self.__next_id = -1

    def __iter__(self):
        """
        When this object is called in for loop, this method's called.

        :return:
        """

        return self

    def __next__(self):
        """
        Gives 'next' message item when for loop is iterating.

        :return:    Message object at corresponding position.
        """

        self.__next_id += 1

        if self.__next_id == len(self.__messages):
            raise StopIteration

        return self.__messages[self.__next_id]

    def getMessages(self):
        """
        Returns all messages.

        :return:    Messages that are saved.
        """

        return self.__messages

    def getErrors(self, last_only=False):
        """
        Returns error messages only.

        :param last_only:   Some may want only last error, some people will want
                            all errors.
        :return:            Error messages (Message object).
        """

        errors = list()

        for message in self.__messages:
            if message.getMessageType() == MessageType.ERROR:
                if last_only:
                    return message

                errors.append(message)

        return errors

    def getErrorsPrintableRepr(self, last_only=False):
        """
        Returns printable version of error messages.
        That means it returns already formatted messages with each below previous
        one.
        They come coloured as well (red with blue color at item that triggered
        message).

        :param last_only:   Some may want only last error, some people will want
                            all errors.
        :return:            Error messages in string format.
        """

        errors = self.getErrors(last_only)
        output = ''

        for i in range(len(errors)):
            output += errors[i].getMessage()

            if i + 1 < len(errors):
                output += '\n'

        return output

    def getWarnings(self):
        """
        Returns warning messages only.

        :return:    Warning messages (Message object).
        """

        warnings = list()

        for message in self.__messages:
            if message.getMessageType() == MessageType.WARNING:
                warnings.append(message)

        return warnings

    def getWarningsPrintableRepr(self):
        """
        Returns printable version of warning messages.
        That means it returns already formatted messages with each below previous
        one.
        They come coloured as well (yellow with blue color at item that triggered
        message).

        :return:            Warning messages in string format.
        """

        warnings = self.getWarnings()
        output = ''

        for i in range(len(warnings)):
            output += warnings[i].getMessage()

            if i + 1 < len(warnings):
                output += '\n'

        return output

    def getInfo(self):
        """
        Returns info messages only.

        :return:    Info messages (Message object).
        """

        info = list()

        for message in self.__messages:
            if message.getMessageType() == MessageType.INFO:
                info.append(message)

        return info

    def getInfoPrintableRepr(self):
        """
        Returns printable version of info messages.
        That means it returns already formatted messages with each below previous
        one. This is special type of message because all info messages are under
        one INFO tag. Reason for that is because they show global information that's
        not tied to source code line and column either caller too.

        :return:            Info messages in string format.
        """

        info = self.getInfo()
        info_color = '\u001b[36m'  # CYAN
        output = '{}INFO:\n'.format(info_color)

        for i in range(len(info)):
            # info is unique compared to error and warning style because all info
            # messages go under one INFO tag!
            output += '\t{}'.format(info[i].getMessage())

            if i + 1 < len(info):
                output += '\n'

        return output

    def append(self, message: Message):
        """
        Appends new message to list of all messages related to one context. In
        addition, it counts error and warning messages with each new message, if
        it's that kind of message.

        :param message:     Message object.
        :return:            Nothing.
        """

        self.__messages.append(message)

        if message.getMessageType() == MessageType.ERROR:
            self.__errors_count += 1
        elif message.getMessageType() == MessageType.WARNING:
            self.__warnings_count += 1

    def errors_occurred(self):
        """
        Checks if there are any error messages.

        :return:    True if there are some errors, false if there're not.
        """

        if self.__errors_count > 0:
            return True

        return False
