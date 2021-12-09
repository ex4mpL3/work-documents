from termcolor import cprint


class Message:
    @staticmethod
    def error_message(error) -> None:
        """
        Shows a message if an error has occurred and
        indicates the name of the caused error with a description

        :param error: Exception object
        :return:
        """
        cprint(f" {error.__class__.__name__} ",
               'red',
               attrs=['concealed', 'reverse'],
               end=' ')
        cprint(f"{error}!", 'red', attrs=['concealed'])

    @staticmethod
    def command_not_found_message(error) -> None:
        """
        Shows a message if the command is not found

        :param error: Exception object
        :return:
        """
        cprint(f" {error.__class__.__name__} ",
               'yellow',
               attrs=['concealed', 'reverse'],
               end=' ')
        cprint(f"{error}!", 'yellow', attrs=['concealed'])

    @staticmethod
    def command_done_message() -> None:
        """
        Shows a message about a successful command
        :return:
        """
        heading = 'CommandAccepted'
        text = 'Команда успешно выполнена'
        cprint(f" {heading} ", 'green', attrs=['concealed',
                                               'reverse'], end=' ')
        cprint(f"{text}!", 'green', attrs=['concealed'])

    @staticmethod
    def input_command_message() -> None:
        """
        Show message when prompted for command

        :return:
        """
        text = 'Введите нужную Вам команду: '
        cprint(f"{text}!", 'white', attrs=['concealed'])

    @staticmethod
    def message(text: str = None, value=None) -> None:
        """
        Show standard message and used for all other cases

        :param text: Optional text to be shown
        :param value:  optional values, if any.
        It is expected to have {} in the text where the values are to be displayed.
        :return:
        """
        heading = ' CommandDone '
        cprint(f"{heading}", 'green', attrs=['concealed',
                                             'reverse'])
        if value is None:
            cprint(f"{text}", 'green', attrs=['concealed'])
        elif isinstance(value, tuple):
            cprint(text.format(*value), 'green', attrs=['concealed'])
        else:
            cprint(text.format(value), 'green', attrs=['concealed'])
