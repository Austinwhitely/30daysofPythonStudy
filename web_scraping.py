# %%
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import re
import io

headers = {"User-Agent": "MyScraperName / 1.0(austinwhitely2 @ gmail.com)"}

# %%

# WEBSCRAPING A WIKIPEDIA PAGE TO CSV FILE


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
    "C:/Users/austi/Documents/GitHub/30daysofPython/files/Outputs/Companies_data.csv",
    index=False,
)
# %%

url = "https://www.bu.edu/president/boston-university-facts-stats/"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

data = soup.find_all("section")[0]
table_titles = data.find_all("span")[0:]
table_titles = [title.text.strip() for title in table_titles]

with open("table_data.json", "w") as file:
    json.dump(table_titles, file, indent=4)

print(table_titles)

# %%

url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"
page = requests.get(url, headers=headers)


html_stream = io.StringIO(page.text)


tables = pd.read_html(html_stream, match="George Washington", flavor="lxml")
df = tables[0]

if isinstance(df.columns, pd.MultiIndex):
    df.columns = ["_".join(col).strip() for col in df.columns]

print(df.head())


# Tried to scrape this wikipedia data using data soup, but the table was too messy so i found a way to extract the data through pandas

# soup = BeautifulSoup(page.text, "html.parser")

# data = soup.find_all("table")[0]
# table_titles = data.find_all("tr")[1:]
# table_titles = [title.text.strip().replace("/n", " ") for title in table_titles]

# df = pd.DataFrame(columns=table_titles)

# column_data = data.find_all("tr")

# for row in column_data[:1]:
#     row_data = row.find_all("td")
#     individual_row_data = [data.text.strip() for data in row_data]

#     length = len(df)
#     df.loc[length] = individual_row_data

# print(df)


# %%
