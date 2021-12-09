from collections import namedtuple
from enum import Enum
from typing import Tuple, Type, Iterator


class Category(Enum):
    DEFAULT = 0,
    EXIT = 1,
    HELP = 2,
    SERVICE = 3,


Command = namedtuple('Command', [
    'name',
    'category',
    'text_result',
    'description'
])


def get_commands_by_category(commands: Tuple[Command], category: Category) -> Iterator[Command]:
    """
    Get a list of commands for the selected category
    """

    def filter_func(command):
        return command.category is category

    return filter(filter_func, commands)


def get_name_commands_by_category(commands: Tuple[Command],
                                  category: Category) -> Iterator[str]:
    """
    Get a list of command names
    """
    cmd_list = list(get_commands_by_category(commands, category))
    return (cmd.name for cmd in cmd_list)


def get_command_descriptions_by_category(commands: Tuple[Command],
                                         category: Category) -> Iterator[str]:
    """
    Get a list of command descriptions
    """
    cmd_list = list(get_commands_by_category(commands, category))
    return (cmd.description for cmd in cmd_list)


def get_info_commands(commands: Tuple[Command], category: Type[Category]) -> Iterator[str]:
    """
    Get information on commands in the form "command - description"
    """
    sep = ' - '
    default_commands = list(get_name_commands_by_category
                            (commands, category.DEFAULT))
    exit_commands = list(get_name_commands_by_category
                         (commands, category.EXIT))
    help_commands = list(get_name_commands_by_category
                         (commands, category.HELP))

    description_def_cmds = list(get_command_descriptions_by_category
                                (commands, category.DEFAULT))
    description_exit_cmds = list(get_command_descriptions_by_category
                                 (commands, category.EXIT))
    description_help_cmds = list(get_command_descriptions_by_category
                                 (commands, category.HELP))

    para_cmd = (
        (default_commands, description_def_cmds),
        (exit_commands, description_exit_cmds),
        (help_commands, description_help_cmds),
    )

    return (sep.join((cmd, desc))
            for para in para_cmd
            for cmd, desc in zip(*para)
            )


commands_list = (
    Command(
        name='p',
        category=Category.DEFAULT,
        text_result='Имя документа: {}',
        description='вывести имя владельца по номеру документа'
    ),
    Command(
        name='s',
        category=Category.DEFAULT,
        text_result='Полка № {}',
        description='вывести номер полки, на которой находится документ по его номеру'
    ),
    Command(
        name='g',
        category=Category.DEFAULT,
        text_result='Тип № {}',
        description='вывести тип документа по его номеру'
    ),
    Command(
        name='l',
        category=Category.DEFAULT,
        text_result='Список всех документов: {}',
        description='вывести список всех документов'
    ),
    Command(
        name='a',
        category=Category.DEFAULT,
        text_result=None,
        description='добавить новый документ в архив'
    ),
    Command(
        name='as',
        category=Category.DEFAULT,
        text_result=None,
        description='добавить новую полку в перечень'
    ),
    Command(
        name='m',
        category=Category.DEFAULT,
        text_result=None,
        description='переместить документ'
    ),
    Command(
        name='d',
        category=Category.DEFAULT,
        text_result=None,
        description='удалить документ из перечня и директории'
    ),
    Command(
        name='pn',
        category=Category.DEFAULT,
        text_result='Список всех документов: {}',
        description='вывести имена владельцев документов'
    ),
    Command(
        name='q',
        category=Category.EXIT,
        text_result=None,
        description='завершить программу'
    ),
    Command(
        name='i',
        category=Category.SERVICE,
        text_result="""
        Стандартные команды: {}
        Для выхода: {}
        Для вызова справки по командам: {}
                    """,
        description=None
    ),
    Command(
        name='h',
        category=Category.HELP,
        text_result='{}',
        description='вывод списка доступных команд'
    ),
)

commands_set = {
                command.name: command
                for command in commands_list
                }

