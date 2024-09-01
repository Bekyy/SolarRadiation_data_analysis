import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
import gdown

# Define the Google Drive folder URL and the local directory to store the files
drive_folder_url = 'https://drive.google.com/drive/folders/1ghrEMrlGn6ROA7KryWWwBXBCw9gERL92'
local_data_folder = 'data'

# Function to download files from Google Drive
def download_files_from_drive(folder_url, local_folder):
    if not os.path.exists(local_folder):
        os.makedirs(local_folder)
    
    # Extract the folder ID from the URL
    folder_id = folder_url.split('/')[-1]
    
    # Construct the download URL
    download_url = f'https://drive.google.com/drive/folders/{folder_id}?usp=sharing'
    
    # Download the files
    gdown.download_folder(download_url, output=local_folder, quiet=False)

# Function to list CSV files in the local directory
def list_csv_files(local_folder):
    return [f for f in os.listdir(local_folder) if f.endswith('.csv')]

# Function to load a CSV file into a DataFrame
@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

# Plotting functions
def plot_time_series(data, columns):
    values = data[columns]
    fig, ax = plt.subplots(figsize=(8, 3))
    values.plot(kind='line', figsize=(8, 3), alpha=0.5, stacked=False, ax=ax)
    ax.set_title('Time Series Plot of ' + ', '.join(columns))
    ax.set_xlabel('Date')
    ax.set_ylabel('Values')
    ax.legend(loc='upper left')
    ax.grid(True)
    st.pyplot(fig)

def plot_hourly_radiation(df, columns, start_index, end_index, title='Hourly Timeseries Radiation'):
    fig, ax = plt.subplots(figsize=(10, 6))
    for col in columns:
        if col in df.columns:
            ax.plot(df.index[start_index:end_index], df[col][start_index:end_index], label=f'Hourly {col}')
        else:
            print(f"Warning: Column '{col}' not found in DataFrame.")
    ax.set_title(title)
    ax.set_xlabel('Date')
    ax.set_ylabel('Value')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

def plot_weekly_radiation(df, columns, title='Weekly Timeseries Radiation'):
    fig, ax = plt.subplots(figsize=(10, 6))
    for col in columns:
        if col in df.columns:
            ax.plot(df.index, df[col], label=f'Weekly {col}')
        else:
            print(f"Warning: Column '{col}' not found in DataFrame.")
    ax.set_title(title)
    ax.set_xlabel('Date')
    ax.set_ylabel('Value')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

def plot_daily_radiation(df, columns, title='Daily Timeseries Radiation'):
    fig, ax = plt.subplots(figsize=(10, 6))
    for col in columns:
        if col in df.columns:
            ax.plot(df.index, df[col], label=f'Daily {col}')
        else:
            print(f"Warning: Column '{col}' not found in DataFrame.")
    ax.set_title(title)
    ax.set_xlabel('Date')
    ax.set_ylabel('Value')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

def plot_monthly_radiation(df, columns, title='Monthly Timeseries Radiation'):
    fig, ax = plt.subplots(figsize=(10, 6))
    for col in columns:
        if col in df.columns:
            ax.plot(df.index, df[col], label=f'Monthly {col}')
        else:
            print(f"Warning: Column '{col}' not found in DataFrame.")
    ax.set_title(title)
    ax.set_xlabel('Date')
    ax.set_ylabel('Value')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

# Main function to run the Streamlit dashboard
def solar_radiation_dashboard():
    st.set_page_config(page_title="Solar Radiation Dashboard",
                       page_icon=":bar_chart:",
                       layout="wide")
    st.title("Solar Radiation Dashboard")

    # Download files from Google Drive
    download_files_from_drive(drive_folder_url, local_data_folder)

    # List CSV files in the local directory
    data_files = list_csv_files(local_data_folder)

    with st.sidebar:
        # Dropdown to select the file from the local directory
        selected_file = st.selectbox("Select a file", options=data_files)

    if selected_file:
        # Load data based on the selected file
        file_path = os.path.join(local_data_folder, selected_file)
        df = load_data(file_path)

        # Convert the 'Timestamp' column to datetime and set it as the index
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        df = df.set_index('Timestamp')

        # Sidebar options for the type of plot
        plot_type = st.sidebar.selectbox("Select Plot Type", ["Hourly", "Daily", "Weekly", "Monthly"])

        # Columns to plot
        columns_to_plot = st.sidebar.multiselect("Select Columns to Plot", df.columns.tolist())

        # Define start and end index for hourly plots (modify as needed)
        start_index = st.sidebar.slider("Select Start Index", 0, len(df)-1, 0)
        end_index = st.sidebar.slider("Select End Index", 0, len(df)-1, 48)

        # Plot based on user selection
        if st.sidebar.button("Generate Plot"):
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
    else:
        st.info("No file selected", icon="ℹ️")
        st.stop()

if __name__ == "__main__":
    solar_radiation_dashboard()
