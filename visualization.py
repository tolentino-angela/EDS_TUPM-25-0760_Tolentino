import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os

# STATIC VISUALIZATION
def plot_anomalies(df):

    os.makedirs("outputs", exist_ok=True)

    plt.figure(figsize=(10,5))

    plt.plot(df["AccX"], label="AccX")

    anomalies = df[df["Anomaly"] == 1]

    plt.scatter(
        anomalies.index,
        anomalies["AccX"],
        color="red",
        label="Anomaly"
    )

    plt.title("Electric Motor Vibration Anomaly Detection")
    plt.legend()

    plt.savefig("outputs/anomaly_plot.png")

    plt.close()

    print("✅ Visualization saved in outputs/")


# ANIMATION 1
def animate_vibration(df):

    fig, ax = plt.subplots(figsize=(10,5))

    x = df.index[:200]
    y = df["AccX"][:200]

    line, = ax.plot([], [], lw=2)

    ax.set_xlim(0, 200)
    ax.set_ylim(y.min(), y.max())

    ax.set_title("Animated Vibration Signal")

    def update(frame):

        line.set_data(x[:frame], y[:frame])

        return line,

    ani = FuncAnimation(
        fig,
        update,
        frames=200,
        interval=50
    )

    ani.save(
        "outputs/animated_vibration.gif",
        writer="pillow"
    )

    plt.close()

    print("✅ Animated vibration GIF saved!")


# ANIMATION 2
def animate_anomalies(df):

    fig, ax = plt.subplots(figsize=(10,5))

    x = df.index[:200]
    y = df["AccX"][:200]

    line, = ax.plot([], [], lw=2)

    ax.set_xlim(0, 200)
    ax.set_ylim(y.min(), y.max())

    ax.set_title("Animated Anomaly Detection")

    def update(frame):

        ax.clear()

        ax.plot(x[:frame], y[:frame], lw=2)

        current = df.iloc[:frame]

        anomalies = current[current["Anomaly"] == 1]

        if not anomalies.empty:

            ax.scatter(
                anomalies.index,
                anomalies["AccX"],
                color="red"
            )

        ax.set_xlim(0, 200)
        ax.set_ylim(y.min(), y.max())

        ax.set_title("Animated Anomaly Detection")

    ani = FuncAnimation(
        fig,
        update,
        frames=200,
        interval=50
    )

    ani.save(
        "outputs/animated_anomalies.gif",
        writer="pillow"
    )

    plt.close()

    print("✅ Animated anomaly GIF saved!")