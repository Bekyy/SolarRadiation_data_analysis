import streamlit as st
import pandas as pd
import plotly.express as px
import os
import sys
import matplotlib.pyplot as plt

# Add the project root directory to the system path for absolute imports
rpath = os.path.abspath('../')
if rpath not in sys.path:
    sys.path.insert(0, rpath)

# Function to plot time series data
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
    st.pyplot()  # Display the plot in the main section

# Function to plot hourly radiation data
def plot_hourly_radiation(df, columns, start_index, end_index, title='Hourly Timeseries Radiation'):
    plt.figure(figsize=(10, 6))
    for col in columns:
        if col in df.columns:
            plt.plot(df.index[start_index:end_index], df[col][start_index:end_index], label=f'Hourly {col}')
        else:
            print(f"Warning: Column '{col}' not found in DataFrame.")
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    st.pyplot()  # Display the plot in the main section

# Function to plot weekly radiation data
def plot_weekly_radiation(df, columns, title='Weekly Timeseries Radiation'):
    plt.figure(figsize=(10, 6))
    for col in columns:
        if col in df.columns:
            plt.plot(df.index, df[col], label=f'Weekly {col}')
        else:
            print(f"Warning: Column '{col}' not found in DataFrame.")
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    st.pyplot()  # Display the plot in the main section

# Function to plot daily radiation data
def plot_daily_radiation(df, columns, title='Daily Timeseries Radiation'):
    plt.figure(figsize=(10, 6))
    for col in columns:
        if col in df.columns:
            plt.plot(df.index, df[col], label=f'Daily {col}')
        else:
            print(f"Warning: Column '{col}' not found in DataFrame.")
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    st.pyplot()  # Display the plot in the main section

# Function to plot monthly radiation data
def plot_monthly_radiation(df, columns, title='Monthly Timeseries Radiation'):
    plt.figure(figsize=(10, 6))
    for col in columns:
        if col in df.columns:
            plt.plot(df.index, df[col], label=f'Monthly {col}')
        else:
            print(f"Warning: Column '{col}' not found in DataFrame.")
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    st.pyplot()  # Display the plot in the main section

# Main function to run the Streamlit dashboard
def solar_radiation_dashboard():
    st.set_page_config(page_title="Solar Radiation Dashboard",
                       page_icon=":bar_chart:",
                       layout="wide")
    st.title("Solar Radiation Dashboard")

    @st.cache_data
    def load_data(file_name: str, file_type: str):
        # Construct the full path to the file
        file_path = os.path.join("data", file_name)
        if file_type == 'xlsx':
            data = pd.read_excel(file_path, engine='openpyxl')
        elif file_type == 'csv':
            data = pd.read_csv(file_path)
        else:
            st.error("Unsupported file format.")
            st.stop()
        return data

    # Listing files in the "data" folder
    data_files = [f for f in os.listdir("data") if f.endswith(('.csv', '.xlsx'))]

    # with st.sidebar:
        # Dropdown to select the file from the "data" folder
    selected_file = st.selectbox("Select a file", options=data_files)

    if selected_file:
        # Determine the file type based on the extension
        file_type = selected_file.split('.')[-1]

        # Load data based on the selected file
        df = load_data(selected_file, file_type)

        # Convert the 'Timestamp' column to datetime and set it as the index
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        df = df.set_index('Timestamp')

        # Generate and display the plots in the main section
        plot_timeseries(df)
    else:
        st.info("No file selected", icon="ℹ️")
        st.stop()

# Function to generate plots based on user input
def plot_timeseries(df):
    # Sidebar options for the type of plot
    plot_type = st.selectbox("Select Plot Type", ["Hourly", "Daily", "Weekly", "Monthly"])

    # Columns to plot
    columns_to_plot = st.multiselect("Select Columns to Plot", df.columns.tolist())

    # Define start and end index for hourly plots (modify as needed)
    start_index = st.slider("Select Start Index", 0, len(df)-1, 0)
    end_index = st.slider("Select End Index", 0, len(df)-1, 48)

    # Plot based on user selection
    if st.button("Generate Plot"):
        if plot_type == "Hourly":
            df = df.resample('H').mean()
            plot_hourly_radiation(df, columns_to_plot, start_index, end_index)
        elif plot_type == "Daily":
            df = df.resample('D').mean()
            plot_daily_radiation(df, columns_to_plot)
        elif plot_type == "Weekly":
            df = df.resample('W').mean()
            plot_weekly_radiation(df, columns_to_plot)
        elif plot_type == "Monthly":
            df = df.resample('M').mean()
            plot_monthly_radiation(df, columns_to_plot)

if __name__ == "__main__":
    solar_radiation_dashboard()
