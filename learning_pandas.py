# %%

import pandas as pd

# import numpy as np

data = pd.read_csv("files/Data/hacker_news.csv")
df = pd.DataFrame(data)

# making pandas series
series_range = df.iloc[0]
series_content = pd.Series(series_range)

title_series = pd.Series(df["title"])

print(title_series)
print(series_content)
print(df.head())
print(df.tail())
print(df[df["title"].str.contains("python", case=False, na=False)])
print(df[df["title"].str.contains("javascript", case=False, na=False)])
print(df.describe())
# %%
