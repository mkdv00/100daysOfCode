import requests
from twilio.rest import Client

api_key = "c4646362a19e75184ddc7b4d95cf11cd"
lat = "55.7522"
lon = "37.6156"
OWM_endpoint = f"https://api.openweathermap.org/data/2.5/onecall"
auth_token = "40704c70850ba4501608f037e2450039"
accouns_sid = "ACa71ec9a386cca2aa5b72e4d19f9a123c"

weather_params = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "exclude": "current, minutely, daily"
}

response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# weather_id = weather_data["hourly"][0]["weather"][0]["id"]
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]

    if int(condition_code) < 700:
        will_rain = True

if not will_rain:
    client = Client(accouns_sid, auth_token)
    message = client.messages.create(
        body="Сегодня нет дождя",
        from_="+15715260268",
        to="+79197834756"
    )
    print(message.status)
