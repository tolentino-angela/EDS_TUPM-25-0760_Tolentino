import matplotlib.pyplot as plt

def plot_anomalies(df):

    plt.figure()
    plt.plot(df.index, df["AccX"], label="AccX")
    
    anomalies = df[df["Anomaly"] == 1]

    plt.scatter(anomalies.index, anomalies["AccX"], color="red", label="Anomaly")

    plt.legend()
    plt.title("Anomaly Detection Result")
    plt.show()