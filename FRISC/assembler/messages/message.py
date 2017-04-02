from FRISC.assembler.messages.message_type import MessageType
from FRISC.assembler.messages.error_type import ErrorType
from FRISC.assembler.messages.warning_type import WarningType
from FRISC.assembler.messages.info_type import InfoType


class Message:
    """
    Builds and keeps messages of three types:
        - error
        - warning
        - info
    When created, they get proper style (color etc.) and text. In addition, they come
    coloured as default.
    """

    def __init__(self, message_type: MessageType, line: int, start: int, message_subtype, trigger='', caller=None):
        """
        Initializes message object and gives corresponding color (depends on MessageType),
        corresponding text (depends on subtype).
        MessageType:
            - Error
            - Warning
            - Info
        Some Message subtypes:
            - UnsupportedCharacter  (ErrorType)
            - UnknownInstruction    (ErrorType)
            etc.
        Errors and warnings get their tags at beginning because information like line,
        start, trigger and caller are related to some of them, and info type of messages
        are not because that are global messages.

        :param message_type:        Type of message such as ErrorType, WarningType,
                                    InfoType.
        :param line:                Line of trigger in the source code.
        :param start:               Column number of place where trigger begins in the
                                    source code.
        :param message_subtype:     Subtypes that define message itself, not priority or
                                    style.
        :param trigger:             Item (string to be exact) that triggered message.
        :param caller:              Context, object, it's self representation that
                                    requested message.
        """

        self.__message_type = message_type
        self.__line = line
        self.__start = start

        if message_type == MessageType.ERROR:
            # set colors at beginning because if we'll use messages, it should anyway be
            # coloured, except INFO...
            error_color = '\u001b[31m'      # RED
            trigger_color = '\u001b[34m'    # BLUE

            self.__message = "{}ERROR at line {}, column {}:\n\t".format(error_color, line, start)

            if message_subtype == ErrorType.UNRECOGNIZED_INSTRUCTION:
                self.__message += 'UnrecognizedInstructionError: instruction \'{}{}{}\' does not exist'\
                    .format(trigger_color, trigger, error_color)
            elif message_subtype == ErrorType.INVALID_INSTRUCTION_FORMAT:
                self.__message += 'InvalidInstructionFormatError: \'{}{}{}\' is not valid instruction format' \
                    .format(trigger_color, trigger, error_color)
            elif message_subtype == ErrorType.UNRECOGNIZED_REGISTER:
                self.__message += 'UnrecognizedRegisterError: register \'{}{}{}\' does not exist' \
                    .format(trigger_color, trigger, error_color)
            elif message_subtype == ErrorType.REGISTER_OUT_OF_RANGE:
                self.__message += 'RegisterOutOfRangeError: index \'{}{}{}\' is out of range' \
                    .format(trigger_color, trigger, error_color)
            elif message_subtype == ErrorType.INTERMEDIATE_OUT_OF_RANGE:
                self.__message += 'IntermediateOutOfRangeError: value \'{}{}{}\' is too big' \
                    .format(trigger_color, trigger, error_color)
            elif message_subtype == ErrorType.OFFSET_OUT_OF_RANGE:
                self.__message += 'OffsetOutOfRangeError: \'{}{}{}\' offset is too big' \
                    .format(trigger_color, trigger, error_color)
            elif message_subtype == ErrorType.UNRECOGNIZED_CONDITION:
                self.__message += 'UnrecognizedConditionError: \'{}{}{}\' is not valid condition' \
                    .format(trigger_color, trigger, error_color)
            elif message_subtype == ErrorType.NONEXISTENT_LABEL:
                self.__message += 'NonexistentLabelError: label \'{}{}{}\' does not exist' \
                    .format(trigger_color, trigger, error_color)
            elif message_subtype == ErrorType.INVALID_LABEL_NAMING:
                self.__message += 'InvalidLabelNamingError: label \'{}{}{}\' has invalid characters' \
                    .format(trigger_color, trigger, error_color)
            elif message_subtype == ErrorType.UNSUPPORTED_CHARACTER:
                self.__message += 'UnsupportedCharacterError: character \'{}{}{}\' is not supported' \
                    .format(trigger_color, trigger, error_color)

            if caller is not None:
                self.__message += "\n\tcaller__{}".format(caller)
        elif message_type == MessageType.WARNING:
            warning_color = '\u001b[32m'    # YELLOW
            trigger_color = '\u001b[34m'    # BLUE

            self.__message = "{}WARNING at line {}, column {}:\n\t".format(warning_color, line, start)

            if message_subtype == WarningType.LABEL_UNUSED:
                self.__message += 'LabelUnusedWarning: label \'{}{}{}\' is excess'\
                    .format(trigger_color, trigger, warning_color)
            elif message_subtype == WarningType.POSSIBLE_MEMORY_LOCATIONS_OUT_OF_RANGE:
                self.__message += 'PossibleMemoryLocationsOutOfRangeWarning: with current memory size, ' \
                                  'it\'s possible program will use memory locations out of range'

            if caller is not None:
                self.__message += "\n\tcaller__{}".format(caller)
        elif message_type == MessageType.INFO:
            # info_color = '\u001b[36m'       # CYAN
            # self.__message = "INFO:\n\t"

            if message_subtype == InfoType.TIME_CREATED:
                pass
            elif message_subtype == InfoType.BUILD_TIME:
                pass

    def getMessageType(self):
        """
        Gives message type information which is important when seeking for priority etc.

        :return:    Returns type of current message.
        """

        return self.__message_type

    def getMessage(self):
        """
        Returns message itself.
        Error and warning messages come with tags, info messages are not.

        :return:    Message, description of current message.
        """
        return self.__message
