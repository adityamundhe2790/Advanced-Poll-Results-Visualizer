import pandas as pd
from textblob import TextBlob

raw_path = "data/raw_poll_data.csv"
cleaned_path = "data/cleaned_poll_data.csv"

def preprocess_data():
    df = pd.read_csv(raw_path)

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df = df.dropna()

    # Add sentiment
    df["Sentiment"] = df["Feedback"].apply(
        lambda x: TextBlob(str(x)).sentiment.polarity
    )

    return df


if __name__ == "__main__":
    df = preprocess_data()
    df.to_csv(cleaned_path, index=False)

    print("✅ Data cleaned and saved!")