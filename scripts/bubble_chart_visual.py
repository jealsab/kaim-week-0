import matplotlib.pyplot as plt
import pandas as pd

def create_bubble_chart(df, x_col, y_col, size_col, title, xlabel, ylabel):
    # Clean NaN values
    df = df.dropna(subset=[x_col, y_col, size_col])
    
    # Check if size_col contains only non-negative values
    if (df[size_col] < 0).any():
        raise ValueError(f"Column '{size_col}' contains negative values. Please ensure all values are non-negative.")
    
    # Ensure the bubble sizes are proportional
    bubble_size = (df[size_col] / df[size_col].max()) * 1000  # Scale for better visualization
    
    # Create the bubble chart
    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(df[x_col], df[y_col], s=bubble_size, c=df[size_col], cmap='viridis', alpha=0.6, edgecolors="w", linewidth=0.5)
    
    # Customize chart
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    # Add a color bar
    plt.colorbar(scatter, label=size_col)
    
    # Set axis limits if necessary
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()

# Example usage
# Assuming df is your DataFrame
