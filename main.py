from data_loader import load_data
from preprocess import preprocess_data
from analysis import detect_anomalies
from visualization import (
    plot_anomalies,
    animate_vibration,
    animate_anomalies
)
import os

def main():

    file_path = "data/raw.csv"

    df = load_data(file_path)
    df = preprocess_data(df)
    df = detect_anomalies(df)

    os.makedirs("outputs/results", exist_ok=True)
    df.to_csv("outputs/results/analyzed_data.csv", index=False)

    plot_anomalies(df)
    animate_vibration(df)
    animate_anomalies(df)

    print("✅ Pipeline completed successfully!")

if __name__ == "__main__":
    main()