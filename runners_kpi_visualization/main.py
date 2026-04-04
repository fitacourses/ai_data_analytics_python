# region 1. TODO-DONE: Import libraries
import pandas as pd
import matplotlib.pyplot as plt
# endregion

# region 2. TODO-DONE: Load data
# read the CSV file into a pandas 
df = pd.read_csv("data.csv") 
# endregion

# region 3. TODO-DONE: Convert time to decimal pace
# split the time column into minutes and seconds separately
parts = df["time"].str.split(":")

# convert the MM:SS time values into decimal minutes
df["pace"] = parts.str[0].astype(int) + (parts.str[1].astype(int) / 60)
# endregion

# region 4. TODO-DONE: Calculate session score components
df["distance_score"] = df["distance"] * 0.17 # distance rewards longer runs
df["pace_score"] = (10.00 - df["pace"]) * 0.6 # pace rewards faster sessions
df["elevation_score"] = (df["elevation"] / 1000) * 8 # pace rewards faster sessions
df["bpm_score"] = (200 - df["bpm"]) * 0.04 # elevation rewards more climbing
# endregion

# region 5. TODO-DONE: Calculate total performance score per session
df["perf_score_session"] = df["distance_score"] + df["pace_score"] + df["elevation_score"] + df["bpm_score"]
# endregion

# region 6. TODO-DONE: Group data by runner
# group by runner and calculate average for each score
grouped = df.groupby("runner")
avg_perf_score = grouped[["distance_score", "pace_score", "elevation_score", "bpm_score"]].mean()
# endregion

# region 7. TODO Build stacked bar chart
# endregion

# region 8. TODO: Customize
# endregion

# region 9. TODO: Show result
# endregion
