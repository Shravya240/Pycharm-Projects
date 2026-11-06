import requests

url = "https://restcountries.com/v3.1/name/India"

response = requests.get(url)
detail = response.json()

for country in detail:
    print(country["name"]["common"])
    print(country["name"]["official"])