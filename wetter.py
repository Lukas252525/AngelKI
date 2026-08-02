import requests
from config import LATITUDE, LONGITUDE


def wetter_laden():

    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={LATITUDE}"
        f"&longitude={LONGITUDE}"
        "&current="
        "temperature_2m,"
        "apparent_temperature,"
        "precipitation,"
        "pressure_msl,"
        "cloud_cover,"
        "wind_speed_10m,"
        "wind_direction_10m"
        "&hourly="
        "temperature_2m,"
        "pressure_msl,"
        "cloud_cover,"
        "precipitation"
        "&forecast_days=2"
        "&timezone=Europe/Berlin"
    )


    daten = requests.get(url).json()


    current = daten["current"]
    hourly = daten["hourly"]


    zeit = current["time"]

    datum = zeit[:10]
    uhrzeit = zeit[11:16]


    # aktuelle Stunde finden
    aktuelle_stunde = None

    for i, t in enumerate(hourly["time"]):

        if t[:13] == zeit[:13]:
            aktuelle_stunde = i
            break


    if aktuelle_stunde is None:
        aktuelle_stunde = 0



    # -------------------------------
    # Temperatur 24h Trend
    # -------------------------------

    temp_aktuell = hourly["temperature_2m"][aktuelle_stunde]


    index_24h = min(
        aktuelle_stunde + 24,
        len(hourly["temperature_2m"]) - 1
    )


    temp_24h = hourly["temperature_2m"][index_24h]


    temperatur_trend = {

        "jetzt": temp_aktuell,

        "zeit_24h":
            hourly["time"][index_24h][11:16],

        "wert_24h":
            temp_24h
    }



    # -------------------------------
    # Bewölkung 6h
    # -------------------------------

    index_6h = min(
        aktuelle_stunde + 6,
        len(hourly["cloud_cover"]) - 1
    )


    bewoelkung_trend = {

        "jetzt":
            hourly["cloud_cover"][aktuelle_stunde],

        "zeit_6h":
            hourly["time"][index_6h][11:16],

        "wert_6h":
            hourly["cloud_cover"][index_6h]

    }



    # -------------------------------
    # Luftdruck 24h
    # -------------------------------

    druck_24h = hourly["pressure_msl"][index_24h]


    luftdruck_trend = {

        "jetzt":
            current["pressure_msl"],

        "zeit_24h":
            hourly["time"][index_24h][:16],

        "wert_24h":
            druck_24h

    }



    # -------------------------------
    # Regen 6h
    # -------------------------------

    regen_6h = sum(
        hourly["precipitation"]
        [aktuelle_stunde:index_6h + 1]
    )


    niederschlag_trend = {

        "stunden": "6h",

        "menge":
            round(regen_6h, 1)

    }



    return {


        "datum": datum,

        "uhrzeit": uhrzeit,


        "temperature_2m":
            current["temperature_2m"],

        "apparent_temperature":
            current["apparent_temperature"],

        "pressure_msl":
            current["pressure_msl"],

        "cloud_cover":
            current["cloud_cover"],

        "wind_speed_10m":
            current["wind_speed_10m"],

        "wind_direction_10m":
            current["wind_direction_10m"],

        "precipitation":
            current["precipitation"],



        # Prognosen

        "temperatur_trend":
            temperatur_trend,

        "bewoelkung_trend":
            bewoelkung_trend,

        "luftdruck_trend":
            luftdruck_trend,

        "niederschlag_trend":
            niederschlag_trend

    }