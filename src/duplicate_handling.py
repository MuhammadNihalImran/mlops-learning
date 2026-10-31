import pandas as pd


def remove_duplicates():
    data = pd.read_csv("data/raw/student_data.csv")

    print("Records before cleaning:", len(data))

    duplicate_count = data.duplicated().sum()
    print("Duplicate records found:", duplicate_count)

    data = data.drop_duplicates()

    print("Records after cleaning:", len(data))

    print("\nCleaned dataset:")
    print(data)


if __name__ == "__main__":
    remove_duplicates()