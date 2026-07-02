import webbrowser
from pprint import pprint
import requests

url = "https://api.restcountries.com/countries/v5/codes.alpha_2/all?pretty=1"


def web_reader(url: str):
    response = requests.get(url)
    if url.endswith(".txt"):
        countries = response.json()
        print(response.status_code)
        return countries
    else:
        countries = response.content
        print(response.status_code)
        return countries


pprint(web_reader(url))
