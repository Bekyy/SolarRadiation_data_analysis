import pandas as pd
import matplotlib.pyplot as plt


def plot_time_series(data, columns):
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