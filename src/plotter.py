import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_alive(csvfile="data/results.csv", out="plots/alive_nodes.png", window=5):
    df = pd.read_csv(csvfile)
    df['alive_smooth'] = df['alive_nodes'].rolling(window=window, min_periods=1, center=True).mean()
    plt.figure(figsize=(8,5))
    plt.plot(df['time'], df['alive_smooth'], label="Alive nodes (smoothed)")
    plt.plot(df['time'], df['alive_nodes'], alpha=0.25, linewidth=1, label="Raw")
    plt.xlabel("Time (rounds)")
    plt.ylabel("Alive nodes")
    plt.legend()
    os.makedirs(os.path.dirname(out), exist_ok=True)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(out, dpi=200)
    plt.close()
