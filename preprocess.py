def preprocess_data(df):

    print("🧹 Cleaning dataset...")

    # remove duplicate rows
    df = df.drop_duplicates()

    # remove missing values
    df = df.dropna()

    print("✅ Preprocessing complete!")

    return df