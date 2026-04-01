# region 1. Load data
import pandas as pd
# pandas "short for pd" reads data and stores table as "df" - dataFrame
df = pd.read_csv("data.csv")
# endregion

# region 2. Validation
# TODO-DONE: count each runner's sessions and store a warning (or empty string) in a dictionary 
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

# region 3. Calculations
# TODO-DONE: group by runner and calculate the stats
stats  = (df.groupby("runner")[["distance", "elevation", "bpm"]].agg({"distance": "sum", "elevation": "sum", "bpm": "mean"}))

# TODO-DONE: 
# add warning column to stats
# look up each runner's string from the warnings dictionary
# set the value in the "warning" column 
stats["warning"] = ""
for runner in stats.index:
    stats.loc[runner, "warning"] = warnings[runner]
# endregion

# region 4. Average pace 
# TODO-DONE:
# split time on ":" to get minutes and seconds
# get elements from parts and convert to ints, divide by 60 to get pace in decimal minutes, store in new column "pace"
# add average pace per runner to stats table

parts = df["time"].str.split(":") 
df["pace"] = parts.str[0].astype(int) + (parts.str[1].astype(int) / 60)
total_time = df.groupby("runner")["pace"].sum()
total_dist = df.groupby("runner")["distance"].sum()
stats["avg_pace"] = total_time / total_dist

# TODO-DONE: convert decimal pace to MM:SS string
for runner in stats.index:
    decimal_pace = stats.loc[runner, "avg_pace"]  # get decimal pace for this runner e.g. 5.86
    minutes = int(decimal_pace)                    # take only the whole number part e.g. 5
    seconds = round((decimal_pace - minutes) * 60) # subtract minutes, multiply leftover by 60 to get seconds e.g. 0.86 * 60 = 52
    stats.loc[runner, "avg_pace"] = f"{minutes}:{seconds:02d}" # combine into MM:SS string, :02d ensures 2 digits e.g. 5:52
# endregion

# region 5. Performance score
# TODO-DONE: calculate performance score for each session
# distance * 0.35 — more km raises score
# 1/pace * 10 * 0.7 — faster pace raises score, 1/pace flips it, *10 scales decimal up
# elevation/50 * 0.6 — more climbing raises score
# bpm/1000 * 0.3 — high heart rate lowers score (penalizes strain)
df["perf_score"] = (df["distance"] * 0.35) + (1/df["pace"] * 10 * 0.7) + (df["elevation"]/50 * 0.6) - (df["bpm"]/1000 * 0.3)

# TODO-DONE: calculate average performance for each runner and store in stats
stats["avg_perf_score"] = df.groupby("runner")["perf_score"].mean()
# endregion

# region 6. Consistency
# TODO-DONE: calculate deviation of runner performance troughout the week(lower = more consistent performance)
stats["consistency"] = df.groupby("runner")["perf_score"].std()
# endregion

# region 7. Winner score
# TODO-DONE: combine average performance and consistency into final ranking
stats["power_ranking"] = (stats["avg_perf_score"] * 0.7) + (1/stats["consistency"] * 0.3)
# endregion

# region 8. Leaderboard
# TODO-DONE: # create daily and weekly leaderboards 
weekly_leaderboard = stats[["avg_perf_score", "consistency", "power_ranking"]].sort_values("power_ranking", ascending=False)

daily_leaderboards = {}                              # empty dictionary to store leaderboard for each day
for day in df["day"].unique():                       # loop through each unique day that exists in the data
    day_df = df[df["day"] == day]                    # filter rows to only this day
    daily_leaderboards[day] = day_df.groupby("runner")["perf_score"].mean().sort_values(ascending=False) # group by runner, get average perf score, sort best first
# endregion

# region 9. Export
# TODO: save stats table to results.xlsx and round numbers

# round stats
stats = stats.round(2)
stats["bpm"] = stats["bpm"].round(1)

# round leaderboards
weekly_leaderboard = weekly_leaderboard.round(2)
for day in daily_leaderboards:
    daily_leaderboards[day] = daily_leaderboards[day].round(2)

with pd.ExcelWriter("results.xlsx") as writer:
    stats.to_excel(writer, sheet_name="Weekly Stats")
    weekly_leaderboard.to_excel(writer, sheet_name="Weekly Leaderboard")
    for day, table in daily_leaderboards.items():
        table.to_excel(writer, sheet_name=str(day))
# endregion
