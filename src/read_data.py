import pandas as pd

def load_data():
    data = pd.read_csv("data/raw/student_data.csv")

    print("Dataset loaded successfully")
    print("\nFirst 5 rows:")
    print(data.head())

    print("\nDataset shape:")
    print(data.shape)

    print("\nDataset information:")
    print(data.info())


if __name__ == "__main__":
    load_data()