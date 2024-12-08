from windrose import WindroseAxes
import matplotlib.pyplot as plt
def plot_wind_rose(df, location):

    
    # Extract wind speed and direction
    wind_speed = df['WS']
    wind_direction = df['WD']
    
    # Create wind rose
    ax = WindroseAxes.from_ax()
    ax.bar(wind_direction, wind_speed, normed=True, opening=0.8, edgecolor='white')
    ax.set_title(f"Wind Rose for {location}")
    ax.set_legend(title="Wind Speed (m/s)")
    plt.show()
