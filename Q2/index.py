import os
import pandas as pd
from glob import glob

FOLDER = "temperatures"

# Month → season mapping
def get_season(month):
    if month in [12, 1, 2]:
        return "Summer"
    elif month in [3, 4, 5]:
        return "Autumn"
    elif month in [6, 7, 8]:
        return "Winter"
    elif month in [9, 10, 11]:
        return "Spring"

# Load all CSVs and reshape
def load_all_data(folder):
    all_files = glob(os.path.join(folder, "*.csv"))
    if not all_files:
        print("No CSV files found.")
        return pd.DataFrame()

    frames = []
    for file in all_files:
        df = pd.read_csv(file)
        # Reshape wide → long
        df_long = df.melt(
            id_vars=["STATION_NAME"],
            value_vars=["January","February","March","April","May","June",
                        "July","August","September","October","November","December"],
            var_name="Month",
            value_name="Temperature"
        )
        df_long["Month_num"] = pd.to_datetime(df_long["Month"], format="%B").dt.month
        df_long["Season"] = df_long["Month_num"].apply(get_season)
        frames.append(df_long)

    return pd.concat(frames, ignore_index=True)

# Seasonal average
def calculate_seasonal_average(df):
    seasonal_avg = df.groupby("Season")["Temperature"].mean().round(1)
    with open("average_temp.txt", "w") as f:
        for season in ["Summer", "Autumn", "Winter", "Spring"]:
            if season in seasonal_avg:
                f.write(f"{season}: {seasonal_avg[season]:.1f}°C\n")

# Largest temp range
def find_largest_temp_range(df):
    stats = df.groupby("STATION_NAME")["Temperature"].agg(["max", "min"])
    stats["range"] = (stats["max"] - stats["min"]).round(1)
    max_range = stats["range"].max()
    top_stations = stats[stats["range"] == max_range]

    with open("largest_temp_range_station.txt", "w") as f:
        for station, row in top_stations.iterrows():
            f.write(f"Station {station}: Range {row['range']:.1f}°C "
                    f"(Max: {row['max']:.1f}°C, Min: {row['min']:.1f}°C)\n")

# Temperature stability
def find_temperature_stability(df):
    stddevs = df.groupby("STATION_NAME")["Temperature"].std().round(1)
    min_std = stddevs.min()
    max_std = stddevs.max()
    most_stable = stddevs[stddevs == min_std]
    most_variable = stddevs[stddevs == max_std]

    with open("temperature_stability_stations.txt", "w") as f:
        for station in most_stable.index:
            f.write(f"Most Stable: Station {station}: StdDev {min_std:.1f}°C\n")
        for station in most_variable.index:
            f.write(f"Most Variable: Station {station}: StdDev {max_std:.1f}°C\n")

def main():
    df = load_all_data(FOLDER)
    if df.empty:
        print("No data loaded.")
        return
    calculate_seasonal_average(df)
    find_largest_temp_range(df)
    find_temperature_stability(df)
    print("Analysis complete. Results saved.")

if __name__ == "__main__":
    main()
