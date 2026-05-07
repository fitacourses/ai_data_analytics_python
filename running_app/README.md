# 🏃 Running Performance Analyzer

> *Streamlit app for analyzing Garmin CSV running data — pace trends, heart rate insights, and coaching signals.*

This project provides a web-based application to analyze running performance data exported from Garmin devices. Upload CSV files to visualize pace trends, estimate personal records, and receive simple coaching recommendations based on pace and heart rate data.

---

## 📌 Overview

This app:

- Processes Garmin CSV activity exports  
- Calculates pace trends and daily summaries  
- Visualizes effort proxy (heart rate vs. pace)  
- Provides coaching insights and records  
- Supports multiple file uploads for combined analysis  
- **Includes local history storage** for comparing data across sessions

The goal is to demonstrate **data analysis** and **interactive visualization** techniques using Python and Streamlit.

---

## 📂 Features

The app includes three main tabs:

- **Overview**: Activity table with configurable rows, key totals (distance, pace), and run type summaries (short <7km, medium 7-13km, long >13km)  
- **Trends**: Cumulative distance chart, pace progression over time (smoothed), distance vs. pace correlation analysis, effort proxy scatter plot (pace vs. heart rate), and elevation gain over time  
- **Insights**: Personal records (fastest pace proxy, longest run streak, most efficient run), last 7 days summary with session type breakdown, acute stress check, recovery readiness assessment, and daily/weekly coaching recommendations with color-coded action boxes  

Example insights:

- Fastest pace estimates (1km proxy)  
- Longest consecutive run streaks  
- Most efficient runs (meters per heartbeat)  
- Effort proxy scatter plots with pace vs. heart rate  
- Coaching signals based on recent training load, intensity, and recovery indicators  
- Local history management for persistent data comparison  

---

## 🛠️ Tools & Libraries

- Python 3  
- Streamlit  
- Pandas  
- Altair  
- Math  

Install dependencies:

```bash
pip install streamlit pandas altair
```

---

## ▶️ How to Run

Navigate to project folder:

```bash
cd running_app
```

Run the app:

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

---

## 📊 Data Source

Data is loaded from Garmin CSV exports containing columns like:

- Activity date  
- Distance (km)  
- Average pace  
- Heart rate (avg/max)  
- Elevation gain/loss  
- Calories  

Upload multiple files to combine data from different periods. The app includes **local history storage** — save uploaded CSVs to disk for persistent comparison across sessions (useful for tracking progress over time).

---

## 🎯 Learning Goals

This project demonstrates:

- Interactive web app development with Streamlit  
- Data cleaning and processing with Pandas  
- Chart creation with Altair  
- User interface design for data analysis  

---

## 📌 Notes

- Supports Latvian language column names in Garmin exports  
- Handles multiple CSV uploads with automatic deduplication  
- Provides guardrails for realistic pace and heart rate values (3-10 min/km pace range)  
- Uses distance-weighted averages to prevent short runs from skewing metrics  
- Includes local history storage for comparing data across app sessions (saved to `.upload_history/` folder)  
- Features adaptive coaching thresholds based on your personal data quantiles  
- Implements smoothed trend lines and correlation analysis for deeper insights</content>
<parameter name="filePath">/home/sandis_linards/workspace/ai_data_analytics_python/running_app/README.md
