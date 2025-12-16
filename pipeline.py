import pandas as pd

def calculate_score(row):
    score = 0

    # Role Fit
    if any(keyword in row["Title"].lower() for keyword in ["toxicology", "safety", "preclinical"]):
        score += 30

    # Company Intent (Funding)
    if row["Funding"] in ["Series A", "Series B"]:
        score += 20

    # Technographic
    if row["Uses_3D_Models"] == "Yes":
        score += 15

    # Location Hub
    if any(hub in row["Location"].lower() for hub in ["boston", "bay", "cambridge"]):
        score += 10

    # Scientific Intent
    if row["Recent_Publication"] == "Yes":
        score += 40

    return min(score, 100)


def process_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["Probability_Score"] = df.apply(calculate_score, axis=1)
    df = df.sort_values(by="Probability_Score", ascending=False)
    df["Rank"] = range(1, len(df) + 1)
    return df
