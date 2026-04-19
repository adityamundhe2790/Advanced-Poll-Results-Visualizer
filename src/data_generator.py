import os
import pandas as pd
import numpy as np

raw_path = "data/raw_poll_data.csv"

def generate_raw_data():
    np.random.seed(42)

    df = pd.DataFrame({
        "Age": np.random.choice(["18-24", "25-34", "35-44"], 300),
        "Gender": np.random.choice(["Male", "Female"], 300),
        "Tool": np.random.choice(["Python", "Excel", "Power BI", "R"], 300),
        "Rating": np.random.randint(1, 6, 300),
        "Feedback": np.random.choice([
            "Great tool", "Very useful", "Not good",
            "Amazing experience", "Could be better", "Loved it"
        ], 300)
    })

    return df


if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)

    df = generate_raw_data()
    df.to_csv(raw_path, index=False)

    print("✅ Raw data generated!")