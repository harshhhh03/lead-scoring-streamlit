import streamlit as st
import pandas as pd
from pipeline import process_data

st.set_page_config(page_title="Lead Scoring Agent", layout="wide")

st.title("🔍 Lead Generation & Probability Scoring Dashboard")
st.write("Demo web agent for identifying and ranking high-intent biotech leads.")

uploaded_file = st.file_uploader("Upload CSV (or use sample data)", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("sample_data.csv")
    st.info("Using sample dataset")

st.subheader("Raw Input Data")
st.dataframe(df)

processed_df = process_data(df)

st.subheader("Ranked Leads (0–100 Probability)")
st.dataframe(processed_df)

st.download_button(
    label="Download Ranked Leads (CSV)",
    data=processed_df.to_csv(index=False),
    file_name="ranked_leads.csv",
    mime="text/csv"
)
