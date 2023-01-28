import requests

parameters = {
    "lat": 0.264850,
    "lon": 32.566800,
    "appid": "69f04e4613056b159c2761a9d9e664d2",
    "exclude": "current,daily"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)

day_weather = response.json()["hourly"][slice(12)]
condition_list = []
for hour in day_weather:
    condition_list.append(hour["weather"][0]["id"])

print(condition_list)

