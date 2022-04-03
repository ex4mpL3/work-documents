from user_interface import Message
from services.work_documents_service import DocumentWork
import exceptions
from data import documents
from services.commands_service import (
    commands_set,
    commands_list,
    Category,
    get_name_commands_by_category,
    get_info_commands,
)


class DocumentWorkController:
    @staticmethod
    def c_get_type_by_number_input_value():
        """
        Command 'g'
        """
        document_number = DocumentWork.get_type_by_number_input_value()
        if document_number:
            return Message.message(text=commands_set['g'].text_result,
                                   value=document_number)
        raise exceptions.TypeNumberNotFound

    @staticmethod
    def c_get_document_owner_by_number():
        """
        Command 'p'
        """
        document_number = DocumentWork.get_owner_by_number_input_value()
        if document_number:
            return Message.message(text=commands_set['p'].text_result,
                                   value=document_number)
        raise exceptions.OwnerNumberNotFound

    @staticmethod
    def c_get_shelf_by_number_input_value():
        """
        Command 's'
        """
        document_number = DocumentWork.get_shelf_by_number_input_value()
        if document_number:
            return Message.message(text=commands_set['s'].text_result,
                                   value=document_number)
        raise exceptions.ShelfNumberNotFound

    @staticmethod
    def c_add_document_with_input_value():
        """
        Command 'a'
        """
        try:
            DocumentWork.add_document_with_input_value()
        except KeyError:
            raise exceptions.AddDocumentFailed

    @staticmethod
    def c_add_shelf_with_input_value():
        """
        Command 'as'
        """
        try:
            DocumentWork.add_shelf_with_input_value()
        except KeyError:
            raise exceptions.AddShelfFailed

    @staticmethod
    def c_move_document_with_input_value():
        """
        Command 'm'
        """
        try:
            DocumentWork.move_document_with_input_value()
        except (KeyError, ValueError):
            raise exceptions.MoveDocumentFailed

    @staticmethod
    def c_delete_document_with_input_value():
        """
        Command 'd'
        """
        try:
            DocumentWork.delete_document_from_all_with_input_value()
        except ValueError:
            raise exceptions.DeleteDocumentFromAllFailed

    @staticmethod
    def c_show_all_owner() -> None:
        """
        Command 'pn'
        """
        document_owners = DocumentWork.get_document_owner(documents_list=documents)
        return Message.message(value='\n'.join(document_owners),
                               text=commands_set['pn'].text_result)

    @staticmethod
    def c_show_all_documents() -> None:
        """
        Command 'l'
        """
        documents_list = DocumentWork.get_all_documents()
        list_documents = (
            ",\t".join(f"{key}: {value}" for key, value in document.items())
            for document in documents_list
        )
        return Message.message(text=commands_set['l'].text_result,
                               value='\n'.join(list_documents))

    @staticmethod
    def c_show_info():
        """
        Command 'i'
        """
        sep = ', '
        default_commands = sep.join(list(get_name_commands_by_category
                                         (commands_list, Category.DEFAULT)))
        exit_commands = sep.join(list(get_name_commands_by_category
                                      (commands_list, Category.EXIT)))
        help_commands = sep.join(list(get_name_commands_by_category
                                      (commands_list, Category.HELP)))

        return Message.message(text=commands_set['i'].text_result,
                               value=(default_commands,
                                      exit_commands,
                                      help_commands))

    @staticmethod
    def c_show_help():
        """
        Command 'h'
        """
        result = list(get_info_commands(commands_list, Category))
        return Message.message(text=commands_set['h'].text_result,
                               value='\n'.join(result))
