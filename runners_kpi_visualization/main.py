# region 1. TODO-DONE: Import and load data
import pandas as pd
df = pd.read_csv("data.csv") # read the CSV file into a pandas DataFrame
# endregion

# region 2. TODO-DONE: Convert time to decimal pace
# split the time column into minutes and seconds separately
parts = df["time"].str.split(":")

# convert the MM:SS time values into decimal minutes
df["pace"] = parts.str[0].astype(int) + (parts.str[1].astype(int) / 60)
# endregion

# region 3. TODO-DONE: Calculate session score components
df["distance_score"] = df["distance"] * 0.17 # distance rewards longer runs
df["pace_score"] = (10.00 - df["pace"]) * 0.6 # pace rewards faster sessions
df["elevation_score"] = (df["elevation"] / 1000) * 8 # pace rewards faster sessions
df["bpm_score"] = (200 - df["bpm"]) * 0.04 # elevation rewards more climbing

# combine all parts into one performance score
df["perf_score"] = df["distance_score"] + df["pace_score"] + df["elevation_score"] + df["bpm_score"]
# endregion

# region 4. TODO: Calculate total performance score per session
# endregion

# region 5. TODO: Group data by runner
# endregion

# region 6. TODO: Build stacked bar chart
# endregion

# region 7. TODO: Customize chart
# endregion

# region 8. TODO: Show result
# endregion
