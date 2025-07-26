# Financial Query Chatbot 💬📊

This project is a simple **Chatbot-style Q&A app** built with **Streamlit**, allowing users to ask predefined questions about financial data for companies like Apple and Microsoft. It reads a CSV file (`financial.csv`) and returns answers from that data in a conversational format.

🔗 **Live App:** [financial-query-bot.streamlit.app](https://financial-query-bot.streamlit.app)

---

## 🔧 Project Structure

- `financial.csv` — Your dataset with financial metrics across fiscal years.
- `financial_analysis.ipynb` — Exploratory data analysis and insights from the dataset.
- `Financial_Chatbot.py` — Streamlit app file that powers the chatbot interface.

---

## 🗂️ Dataset Format

Make sure your `financial.csv` file follows this format:

| Company   | Fiscal Year | Total Revenue | Net Income | Total Assets | Total Liabilities | Cash Flow from Operating Activities |
|-----------|-------------|----------------|------------|---------------|--------------------|--------------------------------------|
| Apple     | 2023        | 383285         | 96995      | 352583        | 267645             | 110543                               |
| Microsoft | 2022        | 198270         | 72738      | 364840        | 198298             | 89034                                |

Use **exact column names** as above. Each row should represent a company in a specific fiscal year.

---

## 💬 How to Use the Chatbot

This isn't a dropdown dashboard. It's designed like a **true chatbot**, where you **click questions** or type them in manually (limited to predefined formats) to get answers like:

- `What was Apple's Net Income in 2023?`
- `How much was the Total Revenue for Microsoft in 2022?`
- `Give me the Total Liabilities of Apple in 2021.`

### ✅ Supported Question Format:
> What was [Company]'s [Metric] in [Fiscal Year]?

Valid metrics:
- Total Revenue  
- Net Income  
- Total Assets  
- Total Liabilities  
- Cash Flow from Operating Activities

Make sure:
- Company name is exact (`Apple`, `Microsoft`)
- Year matches the fiscal year in the CSV

---

## 🧠 Built As Part of

This project was completed as part of the **BCG X Data Science Virtual Experience** on Forage.

---

## 🚀 Running Locally

1. Clone the repo:
   bash
git clone https://github.com/yourusername/financial-query-chatbot.git
cd financial-query-chatbot

2. Run the Streamlit app:
streamlit run Financial_Chatbot.py

---

🤝 Contributions
Pull requests, feature suggestions, and ideas to improve this mini chatbot are always welcome!

---

📬 Contact
Connect with me on [LinkedIn](https://www.linkedin.com/in/alwnshaji)




























