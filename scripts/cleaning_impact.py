import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_cleaning_impact(df, sensors, timestamp_col):
    """Plot time-series data with cleaning impact."""
    df[timestamp_col] = pd.to_datetime(df[timestamp_col])
    df.sort_values(timestamp_col, inplace=True)
    
    for sensor in sensors:
        plt.figure(figsize=(12, 6))
        sns.lineplot(
            data=df, x=timestamp_col, y=sensor, hue='Cleaning',
            palette={0: 'red', 1: 'blue'}, alpha=0.7
        )
        plt.title(f"Impact of Cleaning on {sensor} Over Time")
        plt.xlabel("Time")
        plt.ylabel(sensor)
        plt.legend(title="Cleaning", labels=["Uncleaned", "Cleaned"])
        plt.show()

def print_summary_statistics(df, sensors):
    """Print summary statistics for specified sensors before and after cleaning."""
    print("Summary Statistics for ModA and ModB Before and After Cleaning")
    for sensor in sensors:
        print(f"\n--- {sensor} ---")
        print("Uncleaned:")
        print(df[df['Cleaning'] == 0][sensor].describe())
        print("Cleaned:")
        print(df[df['Cleaning'] == 1][sensor].describe())