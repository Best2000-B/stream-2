import streamlit as st
import pandas as pd

# Set the title of the app
st.title('Excel File Upload and Data Display')

# Create file uploader widget for Excel file
uploaded_file = st.file_uploader("Upload an Excel file", type=['xlsx', 'xls'])

if uploaded_file is not None:
    # Read the Excel file into a DataFrame
    try:
        df = pd.read_excel(uploaded_file, engine='openpyxl')  # Use 'openpyxl' for .xlsx files
        st.write("DataFrame preview:")
        st.dataframe(df)  # Display the DataFrame
    except Exception as e:
        st.error(f"Error reading the Excel file: {e}")



