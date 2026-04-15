# region App Structure

# ===== Imports =====
import streamlit as st
import pandas as pd

# ===== Layout =====
st.title("AI Running Performance Analyzer")
st.caption("Upload your Garmin data to explore trends, records, and training insights.")

# ===== Tabs =====
tab_overview, tab_trends, tab_records, tab_insights = st.tabs(
    ["Overview", "Trends", "Records", "Insights"]
)

with tab_overview:
    st.subheader("Overview")

with tab_trends:
    st.subheader("Trends")

with tab_records:
    st.subheader("Records")

with tab_insights:
    st.subheader("Insights")

# endregion