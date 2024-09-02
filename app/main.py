import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to load a CSV file into a DataFrame
@st.cache_data
def load_data(file):
    return pd.read_csv(file)

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
    fig, ax = plt.subplots(figsize=(10, 4))
    for col in columns:
        if col in df.columns:
            ax.plot(df.index[start_index:end_index], df[col][start_index:end_index], label=f'Hourly {col}')
        else:
            st.warning(f"Warning: Column '{col}' not found in DataFrame.")
    ax.set_title(title)
    ax.set_xlabel('Date')
    ax.set_ylabel('Value')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

def plot_weekly_radiation(df, columns, title='Weekly Timeseries Radiation'):
    fig, ax = plt.subplots(figsize=(10, 4))
    for col in columns:
        if col in df.columns:
            ax.plot(df.index, df[col], label=f'Weekly {col}')
        else:
            st.warning(f"Warning: Column '{col}' not found in DataFrame.")
    ax.set_title(title)
    ax.set_xlabel('Date')
    ax.set_ylabel('Value')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

def plot_daily_radiation(df, columns, title='Daily Timeseries Radiation'):
    fig, ax = plt.subplots(figsize=(10, 4))
    for col in columns:
        if col in df.columns:
            ax.plot(df.index, df[col], label=f'Daily {col}')
        else:
            st.warning(f"Warning: Column '{col}' not found in DataFrame.")
    ax.set_title(title)
    ax.set_xlabel('Date')
    ax.set_ylabel('Value')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

def plot_monthly_radiation(df, columns, title='Monthly Timeseries Radiation'):
    fig, ax = plt.subplots(figsize=(10, 4))
    for col in columns:
        if col in df.columns:
            ax.plot(df.index, df[col], label=f'Monthly {col}')
        else:
            st.warning(f"Warning: Column '{col}' not found in DataFrame.")
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

    # Sidebar options for the type of plot and columns to plot
    with st.sidebar:
        st.header("Upload and Plot Configuration")
        uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
        plot_type = st.selectbox("Select Plot Type", ["Hourly", "Daily", "Weekly", "Monthly"])
        if uploaded_file is not None:
            df = load_data(uploaded_file)
            if 'Timestamp' in df.columns:
                columns_to_plot = st.multiselect("Select Columns to Plot", df.columns.tolist())
                start_index = st.slider("Select Start Index", 0, len(df)-1, 0)
                end_index = st.slider("Select End Index", 0, len(df)-1, 48)
                generate_plot = st.button("Generate Plot")
            else:
                st.error("The uploaded file does not contain a 'Timestamp' column.")
        else:
            st.info("Please upload a CSV file to get started.", icon="ℹ️")

    if uploaded_file is not None and 'Timestamp' in df.columns and generate_plot:
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        df = df.set_index('Timestamp')
        
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
        st.info("Upload a file and configure the plot using the sidebar.", icon="ℹ️")

if __name__ == "__main__":
    solar_radiation_dashboard()
