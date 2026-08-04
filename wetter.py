import requests

from config import LATITUDE, LONGITUDE
from cache import holen, speichern


def windrichtung_text_grad(grad):

    if grad is None:
        return ""

    richtungen = [
        "Nord",
        "Nordost",
        "Ost",
        "Südost",
        "Süd",
        "Südwest",
        "West",
        "Nordwest"
    ]

    index = round(grad / 45) % 8

    return richtungen[index]



def wetter_laden():

    print("WETTER FUNKTION START")


    # ----------------------------------
    # Cache prüfen
    # ----------------------------------

    gespeichert = holen("wetter")

    if gespeichert:

        print("CACHE WETTER")

        return gespeichert



    print("NEUE WETTER API ANFRAGE")



    # ----------------------------------
    # Open-Meteo API
    # ----------------------------------

    url = (
        "https://api.open-meteo.com/v1/forecast?"
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


    try:

        antwort = requests.get(
            url,
            timeout=10
        )

        daten = antwort.json()


    except Exception as e:

        print("WETTER REQUEST FEHLER")
        print(e)

        gespeichert = holen("wetter")

        if gespeichert:
            return gespeichert

        raise Exception(
            "Wetter konnte nicht geladen werden"
        )



    # ----------------------------------
    # API Fehler abfangen
    # ----------------------------------

    if "current" not in daten:

        print("========== API FEHLER ==========")
        print(daten)
        print("================================")


        gespeichert = holen("wetter")

        if gespeichert:

            print("CACHE WETTER ALS FALLBACK")

            return gespeichert


        raise Exception(
            "Keine Wetterdaten verfügbar"
        )



    current = daten["current"]

    hourly = daten["hourly"]



    zeit = current["time"]



    # ----------------------------------
    # Wetterdaten erstellen
    # ----------------------------------

    ergebnis = {


        # aktuelle Werte

        "datum":
            zeit[:10],


        "uhrzeit":
            zeit[11:16],


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


        "wind_direction_text":
            windrichtung_text_grad(
                current["wind_direction_10m"]
            ),


        "precipitation":
            current["precipitation"],



        # Stundenprognose

        "hourly_time":
            hourly["time"],


        "hourly_temperature":
            hourly["temperature_2m"],


        "hourly_pressure":
            hourly["pressure_msl"],


        "hourly_cloud":
            hourly["cloud_cover"],


        "hourly_precipitation":
            hourly["precipitation"]

    }



    # ----------------------------------
    # Cache speichern
    # ----------------------------------

    print("VOR SPEICHERN")


    speichern(
        "wetter",
        ergebnis
    )


    print("WETTER ERGEBNIS:")
    print(ergebnis)



    return ergebnis