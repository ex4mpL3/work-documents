class GetItemFailed(Exception):
    pass


class OwnerNumberNotFound(GetItemFailed):
    def __init__(self):
        super().__init__(
            f"The owner of this document could not be found"
        )


class TypeNumberNotFound(GetItemFailed):
    def __init__(self):
        super().__init__(
            f"The type for this number was not found"
        )


class ShelfNumberNotFound(GetItemFailed):
    def __init__(self):
        super().__init__(
            f"Could not find a shelf for this document"
        )


class AddDocumentFailed(GetItemFailed):
    def __init__(self):
        super().__init__(
            f"This shelf does not exist"
        )


class DeleteDocumentFromDocumentsFailed(GetItemFailed):
    def __init__(self):
        super().__init__(
            f"No document with this number was found in the list of documents"
        )


class DeleteDocumentFromDirectoriesFailed(GetItemFailed):
    def __init__(self):
        super().__init__(
            f"Could not find a document with this number in the directory"
        )


class DeleteDocumentFromAllFailed(GetItemFailed):
    def __init__(self):
        super().__init__(
            f"Could not find a document with this number in the directory"
            f" or list of documents"
        )


class MoveDocumentFailed(GetItemFailed):
    def __init__(self):
        super().__init__(
            f"Could not find this shelf or document"
        )


class AddShelfFailed(GetItemFailed):
    def __init__(self):
        super().__init__(
            f"This shelf already exists!"
        )


class CommandNotFound(GetItemFailed):
    def __init__(self):
        super().__init__(
            f"The command you were looking for was not found"
        )


class CommandNameAlreadyExist(GetItemFailed):
    def __init__(self):
        super().__init__(
            f"This command already exists!"
        )
