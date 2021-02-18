import requests

parameters = {
    "lat": 55.755825,
    "lng": 37.617298,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"]
print(sunrise.split("T")[1].split(":")[0])
