import requests

try:

    url = "https://icanhazdadjoke.com/?format=txt"
    header = {
        "Accept" : "text/plain"
    }

    response = requests.get(url = url, headers = header)
    if response.status_code == 200:
        print(response.text)
    else:
        print("Failed to fetch joke")

except:
    print("Sorry not able to connect with server")