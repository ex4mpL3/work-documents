from typing import Callable, Union
import sys

from exceptions import (
    CommandNameAlreadyExist,
    CommandNotFound,
)
from controller import DocumentWorkController


class CommandManager:
    """
    Command registration class for accessing a command from main
    """
    def __init__(self):
        self._commands = {}

    def register_command(self, name: str, command: Callable) -> None:
        if name in self._commands:
            raise CommandNameAlreadyExist
        self._commands[name] = command

    def get_command_list(self) -> str:
        return ''.join(
            (",\t".join(
                f""f"{key}: {value.__name__}"
                for key, value in self._commands.items()
            ))
        )

    def get_command(self, name: str) -> Union[Callable, CommandNotFound]:
        """
        Get command from list
        """
        try:
            return self._commands[name]
        except KeyError:
            raise CommandNotFound

    def __str__(self):
        return f'{self.get_command_list()}'


dwc = DocumentWorkController()
command_manager = CommandManager()

# Registering a command in the format "command is a controller method that handling this command"
command_manager.register_command("p", dwc.c_get_document_owner_by_number)
command_manager.register_command("s", dwc.c_get_shelf_by_number_input_value)
command_manager.register_command('g', dwc.c_get_type_by_number_input_value)
command_manager.register_command("l", dwc.c_show_all_documents)
command_manager.register_command("a", dwc.c_add_document_with_input_value)
command_manager.register_command("as", dwc.c_add_shelf_with_input_value)
command_manager.register_command("m", dwc.c_move_document_with_input_value)
command_manager.register_command("d", dwc.c_delete_document_with_input_value)
command_manager.register_command("pn", dwc.c_show_all_owner)
command_manager.register_command("q", sys.exit)
command_manager.register_command("i", dwc.c_show_info)
command_manager.register_command("h", dwc.c_show_help)
