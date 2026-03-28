# to import pd as short for pandas for this main
import pandas as pd
# pandas reads data.csv and stores it as a table in df (dataFrame - datu tabula)
df = pd.read_csv("data.csv")

# TODO-DONE: group by runner and calculate total distance, average pace, average heart rate, total elevation
# hint: df.groupby("runner")["kolonna"].sum() / .mean()
kpi = (df.groupby("runner")[["distance", "pace", "bpm", "elevation"]].agg({"distance": "sum", "elevation": "sum","pace": "mean", "bpm": "mean"}))
kpi["bpm"] = kpi["bpm"].round(1) # round bpm to decimal
print(kpi)

# TODO 3: calculate efficiency score per session
# formula: (distance * 0.3) + (1/pace * 10 * 0.4) + (elevation/100 * 0.2) - (bpm/1000 * 0.1)
# hint: df["efficiency"] adds new column during process

df["efficiency"] = (df["distance"] * 0.3) + (1/df["pace"] * 10 * 0.4) + (df["elevation"]/100 * 0.2) - (df["bpm"]/1000 * 0.1)