import streamlit as st
import pandas as pd

# Load and clean data
df = pd.read_csv("your_file.csv")  # Replace with your CSV file
df.columns = df.columns.str.strip()

st.title("📊 Financial Data Explorer")

# Dropdown: Company
companies = sorted(df["Company"].dropna().unique())
selected_company = st.selectbox("Select a Company", companies)

# Dropdown: Fiscal Year
years = sorted(df[df["Company"] == selected_company]["Fiscal Year"].dropna().unique())
selected_year = st.selectbox("Select a Fiscal Year", years)

# Dropdown: Metric
# Automatically list all numeric metric columns except Company and Fiscal Year
metric_columns = [col for col in df.columns if col not in ["Company", "Fiscal Year"]]
selected_metric = st.selectbox("Select a Metric", metric_columns)

# Button to submit
if st.button("Get Result"):
    result = df[
        (df["Company"] == selected_company) &
        (df["Fiscal Year"] == selected_year)
    ][selected_metric]

    if not result.empty:
        st.success(f'{selected_company} - {selected_metric} in {selected_year}: {result.values[0]}')
    else:
        st.warning("No data found for this selection.")
