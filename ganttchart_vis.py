import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
import pandas as pd

# Task data with dependencies and durations
tasks = [
    {"Task": "Architectural Design", "Start": "2024-01-01", "Duration (months)": 6, "Dependencies": None},
    {"Task": "Market Research", "Start": "2024-07-01", "Duration (months)": 4, "Dependencies": "Architectural Design"},
    {"Task": "Environmental Impact Assessment", "Start": "2024-07-01", "Duration (months)": 2, "Dependencies": "Architectural Design"},
    {"Task": "Advertising Campaign Design", "Start": "2024-11-01", "Duration (months)": 2, "Dependencies": "Market Research"},
    {"Task": "Advertising", "Start": "2025-01-01", "Duration (months)": 4, "Dependencies": "Advertising Campaign Design"},
    {"Task": "Sales Period", "Start": "2025-05-01", "Duration (months)": 4, "Dependencies": "Advertising"},
    {"Task": "Underground Work", "Start": "2024-11-01", "Duration (months)": 3, "Dependencies": "Market Research and EIA"},
    {"Task": "Building Homes", "Start": "2025-02-01", "Duration (months)": 6, "Dependencies": "Underground Work"},
    {"Task": "Building Roads", "Start": "2025-02-01", "Duration (months)": 6, "Dependencies": "Underground Work"}
]

# Convert task data into a DataFrame
df = pd.DataFrame(tasks)

# Calculating start and end dates
df["Start Date"] = pd.to_datetime(df["Start"])
df["End Date"] = df["Start Date"] + pd.to_timedelta(df["Duration (months)"] * 30, unit='D')

# Plotting the Gantt Chart
fig, ax = plt.subplots(figsize=(10, 8))
for i, task in df.iterrows():
    ax.barh(task["Task"], (task["End Date"] - task["Start Date"]).days, left=(task["Start Date"] - df["Start Date"].min()).days, color="skyblue")

# Formatting the timeline
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b '%y"))
ax.set_xlabel("Timeline")
ax.set_ylabel("Tasks")
plt.title("Real Estate Project Gantt Chart")
plt.xticks(rotation=45)
plt.grid(axis="x", linestyle="--", alpha=0.7)

plt.tight_layout()
plt.show()
