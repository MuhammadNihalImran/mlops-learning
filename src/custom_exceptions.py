class InvalidDatasetError(Exception):
    pass


def validate_dataset(data):

    if data is None:
        raise InvalidDatasetError("Dataset cannot be empty")

    if len(data) == 0:
        raise InvalidDatasetError("Dataset has no records")

    print("Dataset validation successful")


try:
    validate_dataset([])

except InvalidDatasetError as e:
    print("Validation Error:", e)