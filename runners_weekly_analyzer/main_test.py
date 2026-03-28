import pandas as pd

# test data - Sandis has 13 sessions (should trigger max warning)
test_data = {
    "runner": ["Sandis"] * 13 + ["Krišs"] * 5,
    "day": list(range(1, 14)) + list(range(1, 6)),
    "distance": [10.0] * 18,
    "time": ["60:00"] * 18,
    "elevation": [100] * 18,
    "bpm": [150] * 18
}

df = pd.DataFrame(test_data)

sessions_per_runner = df.groupby("runner")["day"].count()
for runner, count in sessions_per_runner.items():
    if count < 6:
        print(f"{runner}: You haven't ran enough sessions - {count}! Six is minimum. LACE UP!")
    elif count > 11:
        print(f"{runner}: You've ran too many sessions - {count}! Eleven is maximum. You've overworked! Try removing excess sessions.")