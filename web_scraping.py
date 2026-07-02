# %%
import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {"User-Agent": "MyScraperName / 1.0(austinwhitely1 @ gmail.com)"}

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, "html.parser")

table = soup.find_all("table")[0]
#  another way to get the table data
#  soup.find("table", class_="wikitable sortable")

table_titles = table.find_all("th")
table_titles = [title.text.strip() for title in table_titles]


df = pd.DataFrame(columns=table_titles)

column_data = table.find_all("tr")

for row in column_data[1:]:
    row_data = row.find_all("td")
    individual_row_data = [data.text.strip() for data in row_data]

    length = len(df)
    df.loc[length] = individual_row_data

print(df)
df.to_csv(
    "C:/Users/austi/Documents/GitHub/30daysofPython/files/Outputs/Companies_data",
    index=False,
)
# %%
