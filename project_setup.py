import os

# -----------------------------
# 📁 PROJECT STRUCTURE
# -----------------------------
folders = [
    "data",
    "outputs/charts",
    "outputs/reports",
    "src"
]

files = {
    # -----------------------------
    # ROOT FILES
    # -----------------------------
    "README.md": "# 📊 Poll Results Visualizer (Advanced)\n\nProject setup in progress...\n",

    "requirements.txt": """pandas
numpy
plotly
dash
textblob
nltk
""",

    ".gitignore": """__pycache__/
*.pyc
.env
venv/
data/*.csv
""",

    # -----------------------------
    # DATA FILES
    # -----------------------------
    "data/raw_poll_data.csv": "",
    "data/cleaned_poll_data.csv": "",

    # -----------------------------
    # SOURCE FILES
    # -----------------------------
    "src/app.py": """# 🚀 Main Dash App

from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div([
    html.H1("📊 Poll Results Visualizer - Advanced")
])

if __name__ == "__main__":
    app.run(debug=True)
""",

    "src/data_generator.py": """# 📊 Synthetic Data Generator

import pandas as pd
import numpy as np

def generate_data(n=100):
    return pd.DataFrame({
        "Age": np.random.choice(["18-24", "25-34", "35-44"], n),
        "Gender": np.random.choice(["Male", "Female"], n),
        "Tool": np.random.choice(["Python", "Excel", "Power BI", "R"], n),
        "Rating": np.random.randint(1, 6, n),
        "Feedback": np.random.choice([
            "Great", "Bad", "Average", "Excellent", "Needs improvement"
        ], n)
    })
""",

    "src/preprocessing.py": """# 🧹 Data Cleaning

def clean_data(df):
    df = df.drop_duplicates()
    df = df.dropna()
    return df
""",

    "src/analysis.py": """# 📈 Analysis Functions

def get_vote_share(df):
    return df['Tool'].value_counts(normalize=True) * 100
""",

    "src/nlp.py": """# 🤖 NLP Sentiment Analysis

from textblob import TextBlob

def get_sentiment(text):
    return TextBlob(text).sentiment.polarity
"""
}

# -----------------------------
# 📁 CREATE FOLDERS
# -----------------------------
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# -----------------------------
# 📄 CREATE FILES
# -----------------------------
for file_path, content in files.items():
    os.makedirs(os.path.dirname(file_path), exist_ok=True) if "/" in file_path else None
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("✅ Advanced Poll Results Visualizer project created successfully!")