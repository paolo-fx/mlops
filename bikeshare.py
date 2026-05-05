import pandas as pd

DATA_FILE = "bikeshare.csv"

def load_data():
    return pd.read_csv(DATA_FILE)

def main():
    df = load_data()
    print(df.head())

if __name__ == "__main__":
    main()