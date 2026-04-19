# 🤖 NLP Sentiment Analysis
from textblob import TextBlob

def get_sentiment(text):
    return TextBlob(str(text)).sentiment.polarity

def apply_sentiment(df):
    df["Sentiment"] = df["Feedback"].apply(get_sentiment)
    return df
