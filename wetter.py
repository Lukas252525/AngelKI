import requests
from config import LATITUDE, LONGITUDE


def wetter_laden():

    url = (
        "https://api.open-meteo.com/v1/forecast?"
        f"latitude={LATITUDE}"
        f"&longitude={LONGITUDE}"
        "&current=temperature_2m,apparent_temperature,precipitation,pressure_msl,cloud_cover,wind_speed_10m,wind_direction_10m"
        "&hourly=temperature_2m,pressure_msl,cloud_cover,precipitation"
        "&forecast_days=2"
        "&timezone=Europe/Berlin"
    )


    antwort = requests.get(url)

    print("OPEN METEO STATUS:", antwort.status_code)

    daten = antwort.json()

    print("OPEN METEO KEYS:", daten.keys())


    if "current" not in daten:
        raise Exception(
            f"Open Meteo liefert kein current: {daten}"
        )


    current = daten["current"]
    hourly = daten["hourly"]


    zeit = current["time"]


    return {

        "datum": zeit[:10],
        "uhrzeit": zeit[11:16],

        "temperature_2m": current["temperature_2m"],
        "apparent_temperature": current["apparent_temperature"],
        "pressure_msl": current["pressure_msl"],
        "cloud_cover": current["cloud_cover"],
        "wind_speed_10m": current["wind_speed_10m"],
        "wind_direction_10m": current["wind_direction_10m"],
        "precipitation": current["precipitation"],


        "hourly_time": hourly["time"],
        "hourly_temperature": hourly["temperature_2m"],
        "hourly_pressure": hourly["pressure_msl"],
        "hourly_cloud": hourly["cloud_cover"],
        "hourly_precipitation": hourly["precipitation"]

    }