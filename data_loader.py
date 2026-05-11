import pandas as pd

def load_data(file_path):

    print("✅ Dataset loaded successfully!")

    df = pd.read_csv(file_path)

    return df