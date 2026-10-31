import pandas as pd


def validate_dataset(data):
    required_columns = ["name", "age", "marks"]

    # Check required columns
    missing_columns = [
        column for column in required_columns
        if column not in data.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    # Check missing values
    print("Missing values:")
    print(data[required_columns].isnull().sum())

    # Check duplicate records
    print("\nDuplicate records:", data.duplicated().sum())

    # Check data types
    print("\nData types:")
    print(data.dtypes)

    print("\nDataset inspection completed.")


if __name__ == "__main__":
    dataset = pd.read_csv("data/raw/student_data.csv")
    validate_dataset(dataset)