# KPI File Reader — Weekly Running Competition

Python script that reads running data from a CSV file and calculates weekly KPIs and efficiency scores for a group of runners competing against each other.

**Status:** In Progress

---

## Dataset

Weekly training data for 6 runners across 7 days. Each runner logs 6–11 sessions per week, some days with two sessions.

Columns: `runner`, `day`, `distance`, `pace`, `bpm`, `elevation`

---

## KPIs Calculated

- Total distance per runner
- Total elevation gain per runner
- Average pace per runner
- Average heart rate per runner
- Efficiency score per session (based on distance, pace, bpm and elevation)
- Average efficiency per runner — determines the weekly winner
- Best day per runner (highest efficiency score)
- Runner category based on efficiency: Elite / Competitive / Recreational

---

## Stages

1. Load data — read CSV file using pandas
2. Calculations — calculate KPIs for each runner (distance, elevation, pace, bpm)
3. Efficiency — calculate efficiency score per session and average per runner
4. Best day — determine each runner's most efficient training day
5. Leaderboard — print daily or weekly leaderboard based on user input
6. Categories — classify each runner as Elite, Competitive or Recreational
7. Export — save final leaderboard to `results.xlsx` using openpyxl

---

## Requirements

- Max 40 lines of code (excluding comments and blank lines)
- At least one `.txt` or `.csv` file for data storage
- Data aggregation — grouping, summarizing
- At least one `if/elif/else` block
- At least one `for` or `while` loop
- Only `pandas` and `openpyxl` allowed
