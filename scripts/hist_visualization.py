
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_histograms(df, location):
    """Plot histograms for specified meteorological variables."""
    
    # Variables to plot
    variables = ['GHI', 'DNI', 'DHI', 'WS', 'Tamb', 'TModA', 'TModB']
    
    # Clean data by dropping NaN values for the specified variables
    
    # Plot histograms
    for var in variables:
        plt.figure(figsize=(8, 6))
        plt.hist(df[var], bins=30, color='skyblue', edgecolor='black', alpha=0.7)
        plt.title(f"Histogram of {var} in {location}")
        plt.xlabel(var)
        plt.ylabel("Frequency")
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.show()