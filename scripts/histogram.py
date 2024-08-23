import seaborn as sns
import matplotlib.pyplot as plt

def plot_variable_distributions(data, variables, grid_size=(2, 3), figsize=(15, 10), bins=30, color='skyblue'):
    # Setting up the figure and axes
    plt.figure(figsize=figsize)

    for i, var in enumerate(variables):
        plt.subplot(grid_size[0], grid_size[1], i + 1)  # Creating a grid of plots
        sns.histplot(data[var], kde=True, bins=bins, color=color)  # Plotting histogram with KDE
        plt.title(f'Distribution of {var}')
        plt.xlabel(var)
        plt.ylabel('Frequency')

    plt.tight_layout()  # Adjusts spacing between plots
    plt.show()


# Function to calculate Z-scores
def calculate_z_scores(df):
    z_scores = (df - df.mean()) / df.std()
    return z_scores

# Function to flag significant outliers
def flag_outliers(z_scores, threshold=4):
    outliers = (z_scores > threshold) | (z_scores < -threshold)
    return outliers

import matplotlib.pyplot as plt

def plot_timeseries_with_outliers(data, column, outlier_data, title='Time Series with Outliers Highlighted', figsize=(14, 6)):
    plt.figure(figsize=figsize)
    plt.plot(data[column], label=column)
    plt.scatter(outlier_data.index, outlier_data[column], color='red', label='Outliers')
    plt.title(title)
    plt.xlabel('Index')
    plt.ylabel(column)
    plt.legend()
    plt.show()

