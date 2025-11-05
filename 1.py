import pandas as pd
df = pd.read_csv("/workspaces/Week-10-exercise-Analyzing-Weather-Data-with-pandas/weather.csv")
print(df.head(5))
print(df.columns)
print(df.dtypes) 