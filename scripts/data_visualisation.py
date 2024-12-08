import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def prepare_dataframes(df_list):
    """Prepare dataframes by converting 'Timestamp' to datetime and setting it as index."""
    for df in df_list:
    
        # print(df.columns)
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        df.set_index('Timestamp', inplace=True)

def plot_monthly_trends(df, location_name):
    """Plot monthly trends for the specified DataFrame."""
    monthly_avg = df.resample('M')[['GHI', 'DNI', 'DHI', 'Tamb']].mean()
    monthly_avg.plot(figsize=(14, 8), marker='o', title=f"Monthly Trends in {location_name}")
    plt.xlabel("Month")
    plt.ylabel("Average Value")
    plt.legend(['GHI', 'DNI', 'DHI', 'Tamb'])
    plt.grid()
    plt.show()

def plot_daily_patterns(df, location_name):
    """Plot daily patterns for the specified DataFrame."""
    hourly_avg = df.resample('H')[['GHI', 'DNI', 'DHI', 'Tamb']].mean()
    daily_avg = hourly_avg.groupby(hourly_avg.index.hour).mean()
    daily_avg.plot(figsize=(14, 8), marker='o', title=f"Daily Patterns in {location_name}")
    plt.xlabel("Hour of Day")
    plt.ylabel("Average Value")
    plt.legend(['GHI', 'DNI', 'DHI', 'Tamb'])
    plt.grid()
    plt.show()

def detect_and_plot_anomalies(df, column, location_name, threshold_factor=1.5):
    """Detect and plot anomalies for the specified column in the DataFrame."""
    rolling_avg = df[column].rolling(window=24, min_periods=1).mean()
    threshold = threshold_factor * rolling_avg
    anomalies = df[df[column] > threshold]

    plt.figure(figsize=(14, 8))
    plt.plot(df.index, df[column], label=f"{column} Over Time")
    plt.scatter(anomalies.index, anomalies[column], color='red', label="Anomalies", zorder=5)
    plt.title(f"{column} with Anomalies in {location_name}")
    plt.xlabel("Time")
    plt.ylabel(column)
    plt.legend()
    plt.grid()
    plt.show()

def plot_correlation_matrix(df, columns):
    """Plot the correlation matrix for specified columns."""
    plt.figure(figsize=(10, 6))
    correlation_matrix = df[columns].corr()
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm")
    plt.title("Correlation Matrix")
    plt.show()

def plot_pair_plot(df, columns):
    """Plot a pair plot for specified columns."""
    sns.pairplot(df[columns], diag_kind='kde', markers='o')
    plt.suptitle("Pair Plot", y=1.02)
    plt.show()

def plot_wind_vs_solar_scatter(df, wind_columns, solar_columns):
    """Generate scatter plots for wind and solar radiation columns."""
    for wind_col in wind_columns:
        for solar_col in solar_columns:
            plt.figure(figsize=(8, 5))
            sns.scatterplot(data=df, x=wind_col, y=solar_col)
            plt.title(f"Scatter Plot: {solar_col} vs {wind_col}")
            plt.xlabel(wind_col)
            plt.ylabel(solar_col)
            plt.show()