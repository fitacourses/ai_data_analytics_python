# region App Structure

# ===== Imports =====
import streamlit as st
import pandas as pd

# ===== Layout =====
st.title("AI Running Performance Analyzer")
st.caption("Upload your Garmin data to explore trends, records, and training insights.")

# ===== Data Input =====
uploaded_file = st.file_uploader("Upload Garmin CSV file", type=["csv"])

df = None

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

# ===== Tabs =====
tab_overview, tab_trends, tab_records, tab_insights = st.tabs(
    ["Overview", "Trends", "Records", "Insights"]
)

with tab_overview:
    st.subheader("Overview")

    if df is not None:
        st.write("Data loaded successfully.")
        df = df.drop(
    columns=[
        "Unnamed: 0",
        "Soļu veids",
        "Intervāls",
        "Kumulatīvais laiks",
    ]
)

        st.dataframe(df.head())
        st.write(df.columns)

with tab_trends:
    st.subheader("Trends")

with tab_records:
    st.subheader("Records")

with tab_insights:
    st.subheader("Insights")

# endregion