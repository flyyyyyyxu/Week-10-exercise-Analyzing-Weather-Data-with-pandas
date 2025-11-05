import pandas as pd
df = pd.read_csv("/workspaces/Week-10-exercise-Analyzing-Weather-Data-with-pandas/weather.csv")

philly_df = df[df["Station.City"] == "Philadelphia"]

avg_temp = philly_df["Data.Temperature.Avg Temp"].mean()          
max_temp = philly_df["Data.Temperature.Max Temp"].max()           
min_temp = philly_df["Data.Temperature.Min Temp"].min()           
total_precip = philly_df["Data.Precipitation"].sum()             
rainy_days = (philly_df["Data.Precipitation"] > 0).sum()          

print("📍 Station.Cit：Philadelphia")
print(f"Avg Temp：{avg_temp:.2f}°F")
print(f"Max Temp：{max_temp}°F")
print(f"Min Temp：{min_temp}°F")
print(f"Precipitation：{total_precip:.2f} ")
print(f"Precipitation > 0：{rainy_days} 天")