import requests
from config import LATITUDE, LONGITUDE


def mond_laden():

    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={LATITUDE}"
        f"&longitude={LONGITUDE}"
        "&daily=moon_phase,sunrise,sunset"
        "&timezone=Europe/Berlin"
    )

    antwort = requests.get(url)

    daten = antwort.json()

    phase = daten["daily"]["moon_phase"][0]

    if phase < 0.0625 or phase >= 0.9375:
        name = "🌑 Neumond"

    elif phase < 0.1875:
        name = "🌒 zunehmende Sichel"

    elif phase < 0.3125:
        name = "🌓 Erstes Viertel"

    elif phase < 0.4375:
        name = "🌔 zunehmender Mond"

    elif phase < 0.5625:
        name = "🌕 Vollmond"

    elif phase < 0.6875:
        name = "🌖 abnehmender Mond"

    elif phase < 0.8125:
        name = "🌗 Letztes Viertel"

    else:
        name = "🌘 abnehmende Sichel"

    return {
        "wert": phase,
        "name": name,
        "sonnenaufgang": daten["daily"]["sunrise"][0],
        "sonnenuntergang": daten["daily"]["sunset"][0]
    }