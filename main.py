import requests
import smtplib

# For my code to return results with rain i got a place in DRC  called Lombe that has rain
# some hours of the day today from ventusky.com
parameters = {
    "lat": -1.564990,
    "lon": 18.191920,
    "appid": "69f04e4613056b159c2761a9d9e664d2",
    "exclude": "current,daily"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)

weather_slice = response.json()["hourly"][slice(12)]
is_raining = False
for hour_data in weather_slice:
    condition_code = int(hour_data["weather"][0]["id"])
    # checking for conditions less than 700 as API documentations describes them to have rain
    if condition_code < 700:
        is_raining = True

if is_raining:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user='leumaselulak@gmail.com', password="my_app_password")
        connection.sendmail(
            from_addr="leumaselulak@gmail.com",
            to_addrs="kibirigekalules@gmail.com",
            msg="It is going to rain today so carry an umbrella!"
        )


