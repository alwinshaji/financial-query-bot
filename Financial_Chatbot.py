import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("financial.csv")

# Normalize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Info for user
st.title("📊 Financial Query Bot")
st.markdown(
    """
    Ask simple financial questions about the dataset.

    **How to use:**
    - Select a **company**, **fiscal year**, and **question type** below.
    - Ensure your dataset has columns like: `company`, `fiscal_year`, `revenue`, `net_profit`, etc.
    - Keep the column names clean (e.g., use underscores instead of spaces).
    """
)

# Check expected columns exist
required_cols = ["company", "fiscal_year"]
if not all(col in df.columns for col in required_cols):
    st.error("Dataset must include `company` and `fiscal_year` columns (normalized as lowercase with underscores).")
    st.stop()

# Dropdowns
companies = sorted(df["company"].dropna().unique())
years = sorted(df["fiscal_year"].dropna().unique())
questions = [
    "What is the revenue?",
    "What is the net profit?",
    "What is the profit margin?",
    "What are the total expenses?",
]

selected_company = st.selectbox("Select a Company", companies)
selected_year = st.selectbox("Select a Fiscal Year", years)
selected_question = st.selectbox("What do you want to know?", questions)

# Filter based on selections
filtered = df[
    (df["company"] == selected_company) &
    (df["fiscal_year"] == selected_year)
]

# Response logic
if filtered.empty:
    st.warning("No data found for this selection.")
else:
    row = filtered.iloc[0]
    if selected_question == "What is the revenue?":
        st.success(f"📈 Revenue: ₹{row.get('revenue', 'N/A')}")
    elif selected_question == "What is the net profit?":
        st.success(f"💰 Net Profit: ₹{row.get('net_profit', 'N/A')}")
    elif selected_question == "What is the profit margin?":
        try:
            profit_margin = (row['net_profit'] / row['revenue']) * 100
            st.success(f"📊 Profit Margin: {profit_margin:.2f}%")
        except:
            st.error("Couldn't calculate profit margin.")
    elif selected_question == "What are the total expenses?":
        st.success(f"💸 Total Expenses: ₹{row.get('expenses', 'N/A')}")
