import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_csv("financial.csv")

# Convert year column if needed
df['Year'] = df['Year'].astype(str).str.strip().str.lower()
df['Company'] = df['Company'].str.strip().str.lower()
df.columns = [col.strip().lower() for col in df.columns]

# Extract possible options
all_companies = df['Company'].unique().tolist()
all_years = df['Year'].unique().tolist()
all_metrics = [col for col in df.columns if col not in ['company', 'year']]

# Session state for chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Title & usage instructions
st.title("💬 Financial Data Chatbot")

st.markdown("""
**How to ask questions:**

✅ Ask about **Company + Year + Financial Metric**  
Examples:
- _"What is the revenue of Infosys in 2021?"_
- _"Show TCS net profit for FY2022"_
- _"Wipro 2020 all data"_

❌ Avoid vague or incomplete questions.
""")

# Input box
user_input = st.text_input("Ask your question")

# Function to parse the query
def parse_query(query):
    query = query.lower()

    company = next((c for c in all_companies if c in query), None)
    year = next((y for y in all_years if y in query), None)
    metric = next((m for m in all_metrics if m in query), None)

    return company, year, metric

# Handle query
if user_input:
    company, year, metric = parse_query(user_input)

    if not company:
        response = "❗ Please mention a valid company name."
    elif not year:
        response = "❗ Please specify the year or fiscal year."
    else:
        filtered = df[(df['Company'] == company) & (df['Year'] == year)]
        if filtered.empty:
            response = "⚠️ No data found for that combination."
        else:
            if metric:
                value = filtered.iloc[0][metric]
                response = f"✅ {metric.title()} of {company.title()} in {year.title()} is **{value}**"
            else:
                # Show all data for that company and year
                info = filtered.drop(columns=['Company', 'Year']).to_dict(orient='records')[0]
                response = f"📊 Financial Data for {company.title()} in {year.title()}:\n"
                for k, v in info.items():
                    response += f"- **{k.title()}**: {v}\n"

    # Add to chat history
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))

# Show chat history
for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"**🧑‍💻 {sender}:** {message}")
    else:
        st.markdown(f"**🤖 {sender}:** {message}")
