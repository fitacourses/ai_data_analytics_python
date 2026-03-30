# region 1. Load data
import pandas as pd
# pandas "short for pd" reads data and stores table as "df" - dataFrame
df = pd.read_csv("data.csv")
# endregion

# region 2. Validation
# TODO: validate session count per runner (min 6, max 11)

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
# TODO-DONE: group by runner and calculate total distance, average pace, average heart rate, total elevation
stats  = (df.groupby("runner")[["distance", "elevation", "bpm"]].agg({"distance": "sum", "elevation": "sum", "bpm": "mean"}))
stats["warning"] = [warnings[r] for r in stats.index]
# endregion

# region 4. Average pace
# TODO-DONE: 
parts = df["time"].str.split(":") # split time on ":" to get minutes and seconds
# get elements from parts and convert to ints, divide by 60 to get pace in decimal minutes, store in new column "pace"
df["pace"] = parts.str[0].astype(int) + (parts.str[1].astype(int) / 60)
# add average pace per runner to stats table
total_time = df.groupby("runner")["pace"].sum()
total_dist = df.groupby("runner")["distance"].sum()
stats["avg_pace"] = total_time / total_dist
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

# region 6. Best day
# TODO: find the day with highest performance for each runner and store in stats
daily_perf = df.groupby(["runner", "day"])["perf_score"].mean() # get average performance per day
best_day = daily_perf.groupby("runner").idxmax().str[1] # find day with highest average performance, extract day number
stats["best_day"] = best_day
# endregion

# region 7. Consistency
# TODO-DONE: # calculate deviation of runner performance troughout the week(lower = more consistent performance)
stats["consistency"] = df.groupby("runner")["perf_score"].std()
# endregion

# region 8. Winner score
# TODO-DONE: combine average performance and consistency into final ranking
stats["power_ranking"] = (stats["avg_perf_score"] * 0.7) + (1/stats["consistency"] * 0.3)
# endregion

# region 9. Leaderboard
# TODO-DONE: 
weekly_leaderboard = stats[["avg_perf_score", "consistency", "power_ranking"]].sort_values("power_ranking", ascending=False)

# daily leaderboards for each day that exists in the data
daily_leaderboards = {}
for day in df["day"].unique():
    day_df = df[df["day"] == day]
    daily_leaderboards[day] = day_df.groupby("runner")["perf_score"].mean().sort_values(ascending=False)
# endregion

# region 10. Export
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