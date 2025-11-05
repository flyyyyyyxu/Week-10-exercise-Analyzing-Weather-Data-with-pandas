import pandas as pd
df = pd.read_csv("/workspaces/Week-10-exercise-Analyzing-Weather-Data-with-pandas/weather.csv")

station_code = input("Please input Station.Code：").strip()

station_df = df[df["Station.Code"] == station_code]

if station_df.empty:
    print(f"Can't find {station_code} .")
else:
    avg_temp = station_df["Data.Temperature.Avg Temp"].mean()
    total_precip = station_df["Data.Precipitation"].sum()
    avg_wind = station_df["Data.Wind.Speed"].mean()

    # 6. 输出结果
    print(f"\n📍 Station.Code：{station_code}")
    print(f"Avg Temp：{avg_temp:.2f}°F")
    print(f"Precipitation：{total_precip:.2f} ")
    print(f"Wind Speed：{avg_wind:.2f} mph")