import pandas as pd

DATA_FILE = "bikeshare.csv"

def load_data():
    return pd.read_csv(DATA_FILE)

def show_summary(df):
    print("Dataset shape:", df.shape)
    print(df.head())

def main():
    df = load_data()
    show_summary(df)

if __name__ == "__main__":
    main()