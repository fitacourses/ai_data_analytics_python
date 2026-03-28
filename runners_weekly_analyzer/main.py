# to import pd as short for pandas for this main
import pandas as pd
# pandas reads data.csv and stores it as a table in df (dataFrame - datu tabula)
df = pd.read_csv("data.csv")

# TODO-DONE: group by runner and calculate total distance, average pace, average heart rate
# hint: df.groupby("runner")["kolonna"].sum() / .mean()

print(df.groupby("runner")[["distance", "pace", "bpm", "elevation"]].agg({"distance": "sum", "elevation": "sum","pace": "mean", "bpm": "mean"}))