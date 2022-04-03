from user_interface import Message
from command_manager import command_manager
import exceptions


if __name__ == "__main__":
    command_manager.get_command(name='i')()
    while True:
        Message.input_command_message()
        input_command = input().lower()

        try:
            command_manager.get_command(name=input_command)()
        except (
                exceptions.AddShelfFailed,
                exceptions.MoveDocumentFailed,
                exceptions.DeleteDocumentFromDirectoriesFailed,
                exceptions.DeleteDocumentFromDocumentsFailed,
                exceptions.DeleteDocumentFromAllFailed,
                exceptions.AddDocumentFailed,
                exceptions.ShelfNumberNotFound,
                exceptions.OwnerNumberNotFound,
                exceptions.TypeNumberNotFound,
        ) as f:
            Message.error_message(f)
        except exceptions.CommandNotFound as f:
            Message.command_not_found_message(f)
