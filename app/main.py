import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Solar Radiation Dashboard",
                   page_icon=":bar_chart:",
                   layout="wide"
                   )
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

with st.sidebar:
    # Dropdown to select the file from the "data" folder
    selected_file = st.selectbox("Select a file", options=data_files)

    if selected_file:
        # Determine the file type based on the extension
        file_type = selected_file.split('.')[-1]
        
        # Load data based on the selected file
        df = load_data(selected_file, file_type)

        # Display the DataFrame in the app
        #st.write(df)
    else:
        st.info("No file selected", icon="ℹ️")
        st.stop()

# Now you can use `df` for further processing or displaying
st.write(df)