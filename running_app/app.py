# region Imports

import streamlit as st
import pandas as pd

# endregion

# region App Structure

# ===== Layout =====
st.title("AI Running Performance Analyzer")
st.caption("Upload your Garmin data to explore trends, records, and training insights.")

# ===== Data Input =====
uploaded_files = st.file_uploader(
    "Upload Garmin CSV files",
    type=["csv"],
    accept_multiple_files=True
)

# ===== Tabs =====
tab_overview, tab_trends, tab_records, tab_insights = st.tabs(
    ["Overview", "Trends", "Records", "Insights"]
)

# endregion

# region Raw Data Loading

df = None

if uploaded_files:
    # Read each uploaded CSV separately, then combine them into one dataframe
    dataframes = []

    for file in uploaded_files:
        current_df = pd.read_csv(file)

        # Add source file name to track where data comes from
        current_df["source_file"] = file.name

        dataframes.append(current_df)

    df = pd.concat(dataframes, ignore_index=True)

# endregion

# region Data Processing

clean_df = None

if df is not None:
    # Create a clean copy of raw data for processing
    clean_df = df.copy()

    # Remove columns that are technical, duplicated, or not useful for the current analysis
    clean_df = clean_df.drop(
        columns=[
            "Unnamed: 0",
            "Soļu veids",
            "Intervāls",
            "Kumulatīvais laiks",
            "Distance",
        ]
    )

    # Rename key columns to consistent English snake_case names
    # so the rest of the code is easier to read and maintain
    clean_df = clean_df.rename(
        columns={
            "Attālums": "distance_km",
            "Laiks": "duration",
            "Vid. temps": "avg_pace",
            "Vid. SR": "avg_cadence",
            "Maks. SR": "max_cadence",
            "Kopējais kāpums": "elevation_gain",
            "Kopējais kritums": "elevation_loss",
            "Kalorijas": "calories",
            "Labākais temps": "best_pace",
            "Kustības laiks": "moving_time",
            "Vid. kustības temps": "avg_moving_pace",
        }
    )

# endregion

# region KPIs

total_distance = None

if clean_df is not None:
    total_distance = clean_df["distance_km"].sum()

# endregion

# region Overview Tab

with tab_overview:
    st.subheader("Overview")

    if clean_df is not None:
        st.write("Data loaded successfully.")

        if total_distance is not None:
            st.metric("Total Distance (km)", f"{total_distance:.2f}")

        n_rows = st.slider("Rows to display", 5, 100, 20)
        st.dataframe(clean_df.head(n_rows))
        st.write(clean_df.columns)

# endregion

# region Trends Tab

with tab_trends:
    st.subheader("Trends")

# endregion

# region Records Tab

with tab_records:
    st.subheader("Records")

# endregion

# region Insights Tab

with tab_insights:
    st.subheader("Insights")

# endregion