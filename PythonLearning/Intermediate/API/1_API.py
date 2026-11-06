import requests

city = input("Enter the city: ")
url = f"https://wttr.in/{city}"

response = requests.get(url)
print(response.text)


