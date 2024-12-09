import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def analyze_rh_influence(df, location):
    """Analyze the influence of Relative Humidity (RH) on various meteorological variables."""
    
    # Scatter plots with regression lines
    variables = ['Tamb', 'TModA', 'TModB', 'GHI', 'DNI', 'DHI']
    for var in variables:
        plt.figure(figsize=(8, 6))
        sns.regplot(x='RH', y=var, data=df, scatter_kws={'alpha': 0.5}, line_kws={'color': 'red'})
        plt.title(f"Influence of RH on {var} in {location}")
        plt.xlabel("Relative Humidity (%)")
        plt.ylabel(var)
        plt.grid(True)
        plt.show()
    
    # Correlation heatmap
    corr_matrix = df[['RH', 'Tamb', 'TModA', 'TModB', 'GHI', 'DNI', 'DHI']].corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title(f"Correlation Matrix for RH and Other Variables in {location}")
    plt.show()
    
    # Grouped box plots for RH bins
    df['RH_bins'] = pd.cut(df['RH'], bins=[0, 20, 40, 60, 80, 100], labels=['0-20', '20-40', '40-60', '60-80', '80-100'])
    for var in variables:
        plt.figure(figsize=(8, 6))
        sns.boxplot(x='RH_bins', y=var, data=df)
        plt.title(f"{var} Across RH Bins in {location}")
        plt.xlabel("Relative Humidity (%)")
        plt.ylabel(var)
        plt.grid(True)
        plt.show()