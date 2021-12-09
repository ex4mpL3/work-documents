from typing import (
    Iterator,
    List,
    Dict,
    Union,
    Optional,
)

from data import (
    documents,
    directories,
)
from utils import input_arguments_with_prompts


class DocumentWork:
    @staticmethod
    def get_type_by_number(document_number: str) -> Union[str, None]:
        """
        Get document type by document number
        """
        for document in documents:
            if document["number"] == document_number:
                return document["type"]
        return

    @staticmethod
    @input_arguments_with_prompts(
        "Введите номер документа, тип которого вы хотите узнать: ",
    )
    def get_type_by_number_input_value(input_number: str) -> Union[str, None]:
        return DocumentWork.get_type_by_number(input_number)

    @staticmethod
    def get_owner_by_number(document_number: str) -> Union[str, None]:
        """
        Get the name of the person who owns the document
        """
        for document in documents:
            if document["number"] == document_number:
                return document["name"]
        return

    @staticmethod
    @input_arguments_with_prompts(
        "Введите номер документа, владельца которого хотите получить: ",
    )
    def get_owner_by_number_input_value(input_number: str) -> Union[str, None]:
        return DocumentWork.get_owner_by_number(input_number)

    @staticmethod
    def get_all_documents() -> List[Dict[str, str]]:
        """
        Get a list of all documents
        """
        return documents

    @staticmethod
    def get_shelf_by_number(document_number: str) -> Union[str, None]:
        """
        Get shelf number by document number
        """
        for shelf, docs in directories.items():
            for doc in docs:
                if doc == document_number:
                    return shelf
        return

    @staticmethod
    @input_arguments_with_prompts(
        "Введите номер документа, полку на которой она лежит, вы хотите узнать: ",
    )
    def get_shelf_by_number_input_value(document_number: str) -> Union[str, None]:
        return DocumentWork.get_shelf_by_number(document_number=document_number)

    @staticmethod
    def add_document(
            dir_number: str,
            document_type: str,
            document_number: str,
            document_name: str) -> Union[ValueError, None]:
        """
        Add document to catalog and list of shelves, by number, type, owner name
        and the number of the shelf where it will be stored
        """

        if dir_number not in directories:
            raise KeyError

        documents.append(
            {
                "type": document_type,
                "number": document_number,
                "name": document_name,
            }
        )
        directories[dir_number].append(document_number)
        return

    @staticmethod
    @input_arguments_with_prompts(
        "Введите номер полки: ",
        "Введите тип документа: ",
        "Введите номер документа: ",
        "Введите владельца документа: "
    )
    def add_document_with_input_value(
            dir_number: str,
            document_type: str,
            document_number: str,
            document_name: str) -> Union[ValueError, None]:

        return DocumentWork.add_document(
            dir_number,
            document_type,
            document_number,
            document_name,
        )

    @staticmethod
    def delete_document_from_documents(
            document_number: str) -> Union[ValueError, None]:
        """
        Remove a document from the list of documents
        """
        for document in documents:
            if document['number'] == document_number:
                document['number'] = 'Удален'
                return
        raise ValueError

    @staticmethod
    def delete_document_from_directories(
            document_number: str) -> Union[ValueError, None]:
        """
        Удалить документ со с перечня документов
        """
        for directory_value in directories.values():
            if document_number in directory_value:
                directory_value.remove(document_number)
                return
        raise ValueError

    @staticmethod
    @input_arguments_with_prompts(
        "Ведите номер документа, который хотите удалить: ",
    )
    def delete_document_from_all_with_input_value(
            document_number: str) -> (str, int, bool):
        """
        Remove document from catalog or documents
        """
        return DocumentWork.delete_document_from_all(document_number)

    @staticmethod
    def delete_document_from_all(document_number: str):
        """
        Remove document from catalog and documents
        """
        DocumentWork.delete_document_from_directories(document_number)
        DocumentWork.delete_document_from_documents(document_number)

    @staticmethod
    @input_arguments_with_prompts(
        "Ведите номер документа, который хотите удалить: ",
        "Ведите номер полки, куда хотите перенести: "
    )
    def move_document_with_input_value(
            document_number: str,
            another_shelf: str) -> Union[KeyError, None]:
        """
        Move document from current shelf to target shelf
        prompting for input
        """
        return DocumentWork.move_document(document_number, another_shelf)

    @staticmethod
    def move_document(
            document_number: str,
            another_shelf: str) -> Union[KeyError, ValueError, None]:
        """
        Move document from current shelf to target shelf
        """
        try:
            for directory_value in directories.values():
                if document_number in directory_value:
                    directory_value.remove(document_number)
                    directories[another_shelf].append(document_number)
        except (KeyError, ValueError):
            raise
        return

    @staticmethod
    @input_arguments_with_prompts(
        "Введите номер новой полки, которую хотите добавить: "
    )
    def add_shelf_with_input_value(new_shelf: str) -> Optional[KeyError]:
        """
        Add a new shelf to the list asking for input data
        """
        return DocumentWork.add_shelf(new_shelf)

    @staticmethod
    def add_shelf(new_shelf: str) -> Union[KeyError, None]:
        """
        Add a new shelf to the list (directories)
        """
        if new_shelf in directories:
            raise KeyError

        directories[new_shelf] = []
        return

    @staticmethod
    def get_document_owner(documents_list: List[Dict[str, str]]) -> Iterator[str]:
        document_owners = (document["name"] for document in documents_list)
        return document_owners

