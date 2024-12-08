# summary_statistics.py
import pandas as pd

def generate_summary_statistics(df, cols, location):
    """Generate and display summary statistics for the specified DataFrame."""
    print(f"\n=== Summary Statistics for {location} dataset ===")
    
    # Calculate summary statistics
    stats = df[cols].describe()
    
    # Format the output for better readability
    styled_stats = stats.style.set_caption(f'Summary Statistics for {location}') \
                               .set_table_attributes('class="table"') \
                               .highlight_max(axis=0, color='lightgreen') \
                               .highlight_min(axis=0, color='lightcoral')
    
    # Display the styled summary statistics
    display(styled_stats)