import pandas as pd
import streamlit as st

# Load and preprocess the dataset
df = pd.read_csv("financial.csv")
df.columns = df.columns.str.strip()
df['Fiscal Year'] = df['Fiscal Year'].astype(str).str.strip().str.lower()
df['Company'] = df['Company'].astype(str).str.strip().str.lower()
df['Metric'] = df['Metric'].astype(str).str.strip().str.lower()

st.title("💬 Financial Chatbot")
st.write("Ask a financial question about a company and year. Use the format shown in the examples below for best results.")

st.markdown("""
**Examples** (Click to auto-fill):
- Apple Net Income 2023
- Microsoft Revenue 2022
- Google Net Income 2021
""")

# Predefined questions
examples = [
    "Apple Net Income 2023",
    "Microsoft Revenue 2022",
    "Google Net Income 2021"
]

selected_example = st.selectbox("Or select a predefined question:", [""] + examples)
user_input = st.text_input("Type your question here 👇", value=selected_example)

# If user typed or selected something
if user_input:
    with st.chat_message("user"):
        st.write(user_input)

    try:
        parts = user_input.strip().lower().split()
        if len(parts) < 3:
            raise ValueError("Please ask in the format: Company Metric Year")

        company = " ".join(parts[:-2])
        metric = parts[-2]
        year = parts[-1]

        result = df[
            (df['Company'] == company) &
            (df['Metric'] == metric) &
            (df['Fiscal Year'] == year)
        ]

        with st.chat_message("assistant"):
            if not result.empty:
                value = result.iloc[0]['Value']
                st.write(f"{company.title()}'s {metric.title()} in {year}: **{value}**")
            else:
                st.write("Sorry, no data found for that query.")

    except Exception as e:
        with st.chat_message("assistant"):
            st.write("Please follow the format: Company Metric Year (e.g., 'Apple Net Income 2023')")
