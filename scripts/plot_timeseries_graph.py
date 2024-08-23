import pandas as pd
import matplotlib.pyplot as plt


def plot_time_series(data, columns):
    """
    Plots time series area plots for the specified columns in the data. 
    If the columns contain only positive values, it plots a single graph.
    If the columns contain negative values, it plots two graphs:
    one for positive values and one for negative values.

    Parameters:
    - data (DataFrame): The input DataFrame containing the time series data.
    - columns (list): The list of columns to plot.

    Returns:
    None
    """
    values = data[columns]
    
    # Plot positive values
    plt.figure(figsize=(8, 3))
    values.plot(kind='line', figsize=(8, 3), alpha=0.5, stacked=False)
    plt.title('Time Series Plot of ' + ', '.join(columns))
    plt.xlabel('Date')
    plt.ylabel('Values')
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.show()


def plot_hourly_radiation(df, columns, start_index, end_index, title='Hourly Timeseries Radiation'):
    """
    Plot specified columns of hourly data.

    Parameters:
    - df: DataFrame containing the hourly resampled data.
    - columns: List of columns to plot (e.g., ['GHI', 'DNI', 'DHI']).
    - start_index: Starting index for plotting range (default is 0).
    - end_index: Ending index for plotting range (default is 48).
    - title: Title of the plot (default is 'Hourly Timeseries Radiation').

    Returns:
    - None
    """
    plt.figure(figsize=(10, 6))

    # Plot specified columns
    for col in columns:
        if col in df.columns:
            plt.plot(df.index[start_index:end_index], df[col][start_index:end_index], label=f'Hourly {col}')
        else:
            print(f"Warning: Column '{col}' not found in DataFrame.")

    # Customize plot
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_weeky_radiation(df, columns, title='Weekly Timeseries Radiation'):
    """
    Plot specified columns of Weekly data.

    Parameters:
    - df: DataFrame containing the Weekly resampled data.
    - columns: List of columns to plot (e.g., ['GHI', 'DNI', 'DHI']).
    - title: Title of the plot (default is 'Hourly Timeseries Radiation').

    Returns:
    - None
    """
    plt.figure(figsize=(10, 6))

    # Plot specified columns
    for col in columns:
        if col in df.columns:
            plt.plot(df.index, df[col], label=f'Weekly {col}')
        else:
            print(f"Warning: Column '{col}' not found in DataFrame.")

    # Customize plot
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_daily_radiation(df, columns, title='Daily Timeseries Radiation'):
    """
    Plot specified columns of Daily data.

    Parameters:
    - df: DataFrame containing the Daily resampled data.
    - columns: List of columns to plot (e.g., ['GHI', 'DNI', 'DHI']).
    - title: Title of the plot (default is 'Hourly Timeseries Radiation').

    Returns:
    - None
    """
    plt.figure(figsize=(10, 6))

    # Plot specified columns
    for col in columns:
        if col in df.columns:
            plt.plot(df.index, df[col], label=f'Daily {col}')
        else:
            print(f"Warning: Column '{col}' not found in DataFrame.")

    # Customize plot
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.show()    

def plot_Monthly_radiation(df, columns, title='Monthly Timeseries Radiation'):
    """
    Plot specified columns of Monthly data.

    Parameters:
    - df: DataFrame containing the Monthly resampled data.
    - columns: List of columns to plot (e.g., ['GHI', 'DNI', 'DHI']).
    - title: Title of the plot (default is 'Hourly Timeseries Radiation').

    Returns:
    - None
    """
    plt.figure(figsize=(10, 6))

    # Plot specified columns
    for col in columns:
        if col in df.columns:
            plt.plot(df.index, df[col], label=f'Monthly {col}')
        else:
            print(f"Warning: Column '{col}' not found in DataFrame.")

    # Customize plot
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.show()        