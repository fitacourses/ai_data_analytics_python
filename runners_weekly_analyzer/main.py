# region 1. TODO-DONE: Load data
import pandas as pd
df = pd.read_csv("data.csv") # read the CSV file into a pandas DataFrame
# endregion

# region 2. TODO-DONE: Session count check
# count how many sessions each runner has
# store a warning message if the session count is outside the allowed range
sessions_per_runner = df.groupby("runner")["day"].count()
warnings = {}
for runner, count in sessions_per_runner.items():
    if count < 6:
        warnings[runner] = f"Too few sessions ({count})"
    elif count > 11:
        warnings[runner] = f"Too many sessions ({count})"
    else:
        warnings[runner] = ""
# endregion

# region 3. TODO-DONE: Stats calculations
# group rows by runner and calculate the stats
grouped = df.groupby("runner")

stats = grouped[["distance", "elevation", "bpm"]].agg({
    "distance": "sum",
    "elevation": "sum",
    "bpm": "mean"
})
# endregion

# region 3.1. TODO-DONE: Warnings
# add warning column, fill each runner's row with their warning message
stats["warning"] = ""
for runner in stats.index:
    stats.loc[runner, "warning"] = warnings[runner]
# endregion

# region 4. TODO-DONE: Average pace  
# split time column into minutes and seconds separately
parts = df["time"].str.split(":") 

# convert the MM:SS time values into decimal minutes
df["pace"] = parts.str[0].astype(int) + (parts.str[1].astype(int) / 60)

# calculate each runner's average pace by dividing total time by total distance
total_time = df.groupby("runner")["pace"].sum()
total_dist = df.groupby("runner")["distance"].sum()
avg_pace = total_time / total_dist
stats["avg_pace"] = avg_pace
# endregion

# region 4.1. TODO-DONE: Average pace conversion
# allow the avg_pace column to store strings like MM:SS
stats["avg_pace"] = stats["avg_pace"].astype("object")

for runner in stats.index:
    # get this runner's average pace as a decimal number
    decimal_pace = stats.loc[runner, "avg_pace"]

    # take the whole-number part as minutes
    minutes = int(decimal_pace)

    # convert the decimal part into seconds
    seconds = round((decimal_pace - minutes) * 60)

    # format the result as MM:SS
    stats.loc[runner, "avg_pace"] = f"{minutes}:{seconds:02d}"
# endregion

# region 5. TODO-DONE: Performance score
# calculate performance score in new column for each session
# calculate separate score parts for each session
distance_score = df["distance"] * 0.25          # more distance increases score
pace_score = (1 / df["pace"]) * 10 * 1.2        # faster pace increases score
elevation_score = (df["elevation"] / 100) * 0.5 # more elevation increases score
bpm_penalty = (df["bpm"] / 200) * 0.2           # higher heart rate lowers score

# combine all parts into one performance score
df["perf_score"] = distance_score + pace_score + elevation_score - bpm_penalty

# endregion

# region 5.1. TODO-DONE: Average performance score
# calculate each runner's average performance score across all sessions
stats["avg_perf_score"] = df.groupby("runner")["perf_score"].mean()
# endregion

# region 6. TODO-DONE: Consistency
# calculate the standard deviation of each runner's performance scores
# a lower value means the runner was more consistent
stats["consistency"] = df.groupby("runner")["perf_score"].std()
# endregion

# region 7. TODO-DONE: Power ranking
# create the final power ranking score
# average performance has a bigger weight, while consistency also helps
performance_weight = stats["avg_perf_score"] * 0.7
consistency_weight = (1 / stats["consistency"]) * 0.3
stats["power_ranking"] = performance_weight + consistency_weight

# endregion

# region 8. TODO-DONE: Leaderboard
# sort runners by power ranking from highest to lowest
weekly_leaderboard = stats[["avg_perf_score", "consistency", "power_ranking"]].sort_values("power_ranking", ascending=False)

# create a separate leaderboard for each day
daily_leaderboards = {}
# loop through each day name once
for day in df["day"].unique(): 
    # filter rows to only this iterated day
    day_df = df[df["day"] == day] 
    # calculate average performance score for each runner on this day
    daily_scores = day_df.groupby("runner")["perf_score"].mean()
    # sort runners from highest to lowest score
    daily_leaderboard = daily_scores.sort_values(ascending=False)
        # store this day's leaderboard in the dictionary
    daily_leaderboards[day] = daily_leaderboard
# endregion

# region 9. TODO-DONE: Rounding numbers
# round numeric values in stats table
stats = stats.round(2)

# round bpm separately to 1 decimal place
stats["bpm"] = stats["bpm"].round(1)

# round weekly leaderboard values
weekly_leaderboard = weekly_leaderboard.round(2)

# round each daily leaderboard
for day in daily_leaderboards:
    daily_leaderboards[day] = daily_leaderboards[day].round(2)
# endregion

# region 10. TODO-DONE: Export
# write all tables to results.xlsx, each on its own sheet
with pd.ExcelWriter("results.xlsx") as writer:
    stats.to_excel(writer, sheet_name="Weekly Stats")
    weekly_leaderboard.to_excel(writer, sheet_name="Weekly Leaderboard")

    # write each daily leaderboard to its own sheet
    for day, table in daily_leaderboards.items():
        table.to_excel(writer, sheet_name=str(day))
# endregion
# endregion
