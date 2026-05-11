import numpy as np

def detect_anomalies(df):

    print("📊 Running anomaly detection...")

    # acceleration magnitude
    df["AccMagnitude"] = np.sqrt(
        df["AccX"]**2 +
        df["AccY"]**2 +
        df["AccZ"]**2
    )

    # z-score
    mean = df["AccMagnitude"].mean()
    std = df["AccMagnitude"].std()

    df["Z_score"] = (
        df["AccMagnitude"] - mean
    ) / std

    # anomaly threshold
    df["Anomaly"] = df["Z_score"].apply(
        lambda x: 1 if abs(x) > 3 else 0
    )

    print("✅ Anomaly detection complete!")

    return df