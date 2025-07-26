import streamlit as st
import pandas as pd

# Load your data
df = pd.read_csv("financial.csv")  # Replace with your actual file name

# Clean column names
df.columns = df.columns.str.strip()

# Set chatbot title
st.title("📊 Financial Chatbot")

# Predefined question options
questions = {
    "1️⃣ What was Apple's Total Revenue in 2023?": 
        lambda: df[(df['Company'] == 'Apple') & (df['Fiscal Year'] == 2023)]['Total Revenue'].values[0],

    "2️⃣ What was Microsoft's Net Income in 2022?": 
        lambda: df[(df['Company'] == 'Microsoft') & (df['Fiscal Year'] == 2022)]['Net Income'].values[0],

    "3️⃣ What are Apple's Total Assets in 2021?": 
        lambda: df[(df['Company'] == 'Apple') & (df['Fiscal Year'] == 2021)]['Total Assets'].values[0],

    "4️⃣ What was Microsoft's Cash Flow from Operations in 2023?": 
        lambda: df[(df['Company'] == 'Microsoft') & (df['Fiscal Year'] == 2023)]['Cash Flow from Operating Activities'].values[0],

    "5️⃣ What are Apple's Total Liabilities in 2022?": 
        lambda: df[(df['Company'] == 'Apple') & (df['Fiscal Year'] == 2022)]['Total Liabilities'].values[0],
}

# Chat-style UI
st.write("### Ask a question:")
for question, func in questions.items():
    if st.button(question):
        try:
            answer = func()
            st.success(f"Answer: {answer:,}")
        except Exception as e:
            st.error("Something went wrong. Check your data.")

# Optional: Show data
with st.expander("Show Raw Data"):
    st.dataframe(df)
