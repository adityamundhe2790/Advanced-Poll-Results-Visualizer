# 📈 Analysis Functions

def vote_count(df):
    return df["Tool"].value_counts()

def vote_percentage(df):
    return (df["Tool"].value_counts(normalize=True) * 100).round(2)

def demographic_analysis(df):
    return df.groupby(["Age", "Tool"]).size().unstack(fill_value=0)
