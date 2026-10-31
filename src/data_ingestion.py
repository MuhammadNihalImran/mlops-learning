import logging
import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class DataIngestionError(Exception):
    """Raised when data ingestion fails."""


def load_data(file_path):
    try:
        logging.info("Loading dataset from %s", file_path)

        data = pd.read_csv(file_path)

        logging.info("Dataset loaded successfully")
        return data

    except (OSError, pd.errors.ParserError) as error:
        logging.exception("Failed to load dataset")
        raise DataIngestionError(
            f"Could not load dataset: {file_path}"
        ) from error


def validate_data(data):
    required_columns = ["name", "age", "marks"]

    logging.info("Validating dataset")

    if data.empty:
        raise DataIngestionError("Dataset is empty")

    missing_columns = [
        column
        for column in required_columns
        if column not in data.columns
    ]

    if missing_columns:
        raise DataIngestionError(
            f"Missing columns: {missing_columns}"
        )

    logging.info("Dataset validation successful")


def clean_data(data):
    logging.info("Cleaning dataset")

    data = data.copy()

    # Convert numeric columns to numeric types.
    data["age"] = pd.to_numeric(
        data["age"], errors="coerce"
    )
    data["marks"] = pd.to_numeric(
        data["marks"], errors="coerce"
    )

    # Remove duplicate records.
    data = data.drop_duplicates()

    # Fill missing numeric values with column means.
    for column in ["age", "marks"]:
        if data[column].isna().all():
            raise DataIngestionError(
                f"Column '{column}' has no valid numeric values"
            )

        data[column] = data[column].fillna(
            data[column].mean()
        )

    logging.info("Data cleaning completed")
    return data


def run_ingestion(file_path):
    data = load_data(file_path)
    validate_data(data)
    data = clean_data(data)

    logging.info(
        "Ingestion completed. Final records: %d",
        len(data)
    )

    return data


if __name__ == "__main__":
    try:
        dataset = run_ingestion(
            "data/raw/student_data.csv"
        )

        print("\nFinal dataset:")
        print(dataset)

        print("\nMissing values:")
        print(dataset.isnull().sum())

        print("\nDuplicate records:", dataset.duplicated().sum())

    except DataIngestionError as error:
        logging.error("Pipeline failed: %s", error)