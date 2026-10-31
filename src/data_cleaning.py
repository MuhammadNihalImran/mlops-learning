import pandas as pd

def clean_data():
    data = pd.read_csv("data/raw/student_data.csv")

    print("Missing values before cleaning:")
    print(data.isnull().sum())

    # Fill missing numerical values with column means
    data["age"] = data["age"].fillna(data["age"].mean())
    data["marks"] = data["marks"].fillna(data["marks"].mean())

    print("\nMissing values after cleaning:")
    print(data.isnull().sum())

    print("\nCleaned dataset:")
    print(data)

if __name__ == "__main__":
    clean_data()