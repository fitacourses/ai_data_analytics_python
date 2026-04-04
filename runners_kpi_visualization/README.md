# 📌 Runner Performance Visualization Project

## 📌 Overview

This project reads weekly running session data from a CSV file and creates a stacked bar chart to compare average runner performance.

The visualization is based on a custom performance score made from four components:

- Distance score
- Pace score
- Elevation score
- Heart rate score

Each session is scored individually first, then the average score is calculated for each runner. This makes the comparison clearer and helps show what contributes to each runner’s overall result.

---

## 📂 Dataset Format (`data.csv`)

Your input file **must include the following columns**:

| Column     | Description                  |
|------------|------------------------------|
| runner     | Runner's name                |
| day        | Day of the week              |
| distance   | Distance run (km)            |
| time       | Duration in MM:SS            |
| elevation  | Elevation gain (m)           |
| bpm        | Average heart rate (bpm)     |

✅ Each row represents **one running session**.

---

## 📊 Score Components the Script Calculates

### ✅ Distance Score

Rewards longer running distance.

### ✅ Pace Score

Rewards faster pace.

### ✅ Elevation Score

Rewards sessions with more climbing.

### ✅ Heart Rate Score

Rewards lower average heart rate.

---

### ✅ Total Performance Score

Each session gets a total performance score based on all four score components.

---

### ✅ Average Performance Score per Runner

After scoring each session, the script calculates the average score for each runner.

This gives a clearer overall comparison than looking at single sessions one by one.

---

## ⚙️ Script Workflow (Step-By-Step)

1. Load data from CSV  
2. Convert `MM:SS` time values into decimal pace  
3. Calculate score components for each session  
4. Calculate total performance score per session  
5. Group data by runner  
6. Calculate average score contribution per runner  
7. Build a stacked bar chart  
8. Customize the chart for readability  
9. Display the final visualization  

---

## 📈 Output

✅ The script displays a **stacked bar chart** where:

- Each bar represents one runner  
- The total bar height represents average performance score  
- Each colored section shows the contribution of one score component  

This makes it easier to compare runners and understand what influenced their final score.

---

## 🛠 Requirements

You will need:

- Python 3.10+
- pandas
- matplotlib
- A valid `data.csv` file

---

## 🎓 Assignment Requirements Covered

This project includes:

- ✅ File reading  
- ✅ Data processing  
- ✅ Data aggregation  
- ✅ Data visualization  
- ✅ Use of `pandas` and `matplotlib`