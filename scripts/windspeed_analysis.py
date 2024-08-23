import numpy as np
import matplotlib.pyplot as plt

def plot_wind_speed_direction(data, speed_col='WS', direction_col='WD', cmap='viridis', alpha=0.75, figsize=(8, 8), title='Wind Speed and Direction Distribution'):
    # Extract wind speed and direction
    wind_speed = data[speed_col]
    wind_direction = data[direction_col]

    # Convert wind direction from degrees to radians
    wind_direction_radians = np.deg2rad(wind_direction)

    # Create the polar plot
    plt.figure(figsize=figsize)
    ax = plt.subplot(111, projection='polar')

    # Create a scatter plot on the polar axis
    sc = ax.scatter(wind_direction_radians, wind_speed, c=wind_speed, cmap=cmap, alpha=alpha)

    # Add a color bar
    plt.colorbar(sc, label='Wind Speed (m/s)')

    # Set the zero degree location to North and direction of angles to be clockwise
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)

    # Add the title and show the plot
    plt.title(title)
    plt.show()

def plot_wind_rose(data, speed_col='WS', direction_col='WD', num_bins=16, bin_color='skyblue', edge_color='black', figsize=(8, 8), title='Wind Rose: Distribution of Wind Speed and Direction'):
    # Extract wind speed and direction
    wind_speed = data[speed_col]
    wind_direction = data[direction_col]

    # Convert wind direction from degrees to radians
    wind_direction_radians = np.deg2rad(wind_direction)

    # Create the polar plot
    plt.figure(figsize=figsize)
    ax = plt.subplot(111, projection='polar')

    # Create bins for wind direction
    bins = np.linspace(0, 2 * np.pi, num_bins + 1)

    # Compute the histogram
    hist, bin_edges = np.histogram(wind_direction_radians, bins=bins, weights=wind_speed)

    # Create a bar plot on the polar axis
    bars = ax.bar(bin_edges[:-1], hist, width=(2 * np.pi) / num_bins, color=bin_color, edgecolor=edge_color)

    # Set the zero degree location to North and direction of angles to be clockwise
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)

    # Add the title and show the plot
    plt.title(title)
    plt.show()


