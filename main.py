import pandas as pd

df = pd.read_csv("/workspaces/Week-10-exercise-Analyzing-Weather-Data-with-pandas/weather.csv")

print(df.head(5))

print(df.columns)

print(df.dtypes) 


philly_df = df[df["Station.City"] == "Philadelphia"]

avg_temp = philly_df["Temperature"].mean()
max_temp = philly_df["Temperature"].max()
min_temp = philly_df["Temperature"].min()
total_precip = philly_df["Precipitation"].sum()
rainy_days = (philly_df["Precipitation"] > 0).sum()

print("📍 站点：Philadelphia")
print(f"平均温度：{avg_temp:.2f}")
print(f"最高温度：{max_temp}")
print(f"最低温度：{min_temp}")
print(f"总降水量：{total_precip:.2f}")
print(f"降雨天数：{rainy_days}")