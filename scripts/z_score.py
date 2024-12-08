import pandas as pd
from scipy.stats import zscore
import matplotlib.pyplot as plt

def calculate_z_scores(df, columns, location, threshold=3):
  
    zscore_results = {}
    
    for col in columns:

            # Calculate Z-scores
            z_scores = zscore(df[col])
            
            # Create a flag for outliers
            is_outlier = (z_scores > threshold) | (z_scores < -threshold)
            
            # Store results
            zscore_results[col] = {
                "Z-Scores": z_scores,
                "Outliers": is_outlier.sum(),
            }
            
            # Print summary
            print(f"Z-Score Analysis for {col} in {location}:")
            print(f"- Mean: {df[col].mean():.2f}, Std Dev: {df[col].std():.2f}")
            print(f"- Outliers Detected: {is_outlier.sum()} out of {len(df)} rows")
            print("-" * 40)
            
            # Visualize Z-scores
            plt.figure(figsize=(8, 6))
            plt.scatter(range(len(z_scores)), z_scores, c=is_outlier, cmap='coolwarm', alpha=0.7)
            plt.axhline(y=threshold, color='red', linestyle='--', label=f"Threshold (+{threshold})")
            plt.axhline(y=-threshold, color='blue', linestyle='--', label=f"Threshold (-{threshold})")
            plt.title(f"Z-Scores for {col} in {location}")
            plt.xlabel("Data Point Index")
            plt.ylabel("Z-Score")
            plt.legend()
            plt.grid(alpha=0.5, linestyle='--')
            plt.show()