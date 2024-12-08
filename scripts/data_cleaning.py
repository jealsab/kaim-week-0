import pandas as pd

def drop_negative_values(df, columns):
    """Drop rows with negative values for specified columns."""
    cleaned_df = df.copy()
    for col in columns:
        cleaned_df = cleaned_df[cleaned_df[col] >= 0]  # Keep only non-negative values in the specified columns
    return cleaned_df


def drop_missing_values(df, columns):
    """Drop rows with missing values for specified columns."""
    # Drop rows with missing values in the specified columns
    cleaned_df = df.dropna(subset=columns)
    return cleaned_df


def drop_outliers_iqr(df, columns):
    """Remove rows with outliers based on the IQR method for specified columns."""
    cleaned_df = df.copy()
    
    for col in columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        # Drop rows where the value is outside the IQR bounds
        cleaned_df = cleaned_df[(cleaned_df[col] >= lower_bound) & (cleaned_df[col] <= upper_bound)]
    
    return cleaned_df


def clean_data(df, cols):
    """Clean the DataFrame by dropping negative values, missing values, and outliers."""
    # Drop negative values
    df = drop_negative_values(df, cols)
    
    # Drop missing values
    df = drop_missing_values(df, cols)
    
    # Drop outliers using IQR
    df = drop_outliers_iqr(df, cols)
    
    return df
