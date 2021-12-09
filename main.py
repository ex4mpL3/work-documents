from user_interface import Message
from command_manager import command_manager
from exceptions import (
    AddShelfFailed,
    MoveDocumentFailed,
    DeleteDocumentFromDirectoriesFailed,
    DeleteDocumentFromDocumentsFailed,
    DeleteDocumentFromAllFailed,
    AddDocumentFailed,
    ShelfNumberNotFound,
    OwnerNumberNotFound,
    CommandNotFound,
    TypeNumberNotFound,
)


if __name__ == "__main__":
    command_manager.get_command(name='i')()
    while True:
        Message.input_command_message()
        input_command = input().lower()

        try:
            command_manager.get_command(name=input_command)()
        except (
                AddShelfFailed,
                MoveDocumentFailed,
                DeleteDocumentFromDirectoriesFailed,
                DeleteDocumentFromDocumentsFailed,
                DeleteDocumentFromAllFailed,
                AddDocumentFailed,
                ShelfNumberNotFound,
                OwnerNumberNotFound,
                TypeNumberNotFound,
        ) as f:
            Message.error_message(f)
        except CommandNotFound as f:
            Message.command_not_found_message(f)
