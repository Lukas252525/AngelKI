import requests
from config import LATITUDE, LONGITUDE


def luftdrucktrend_laden():

    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={LATITUDE}"
        f"&longitude={LONGITUDE}"
        "&hourly=pressure_msl"
        "&past_hours=24"
        "&forecast_hours=1"
        "&timezone=Europe/Berlin"
    )

    daten = requests.get(url).json()

    print(daten)

    druck = daten["hourly"]["pressure_msl"]

    erster = druck[0]
    letzter = druck[-1]

    differenz = round(letzter - erster, 1)

    if differenz >= 2:
        trend = "↗ Steigend"

    elif differenz <= -2:
        trend = "↘ Fallend"

    else:
        trend = "→ Stabil"

    return {
        "trend": trend,
        "differenz": differenz,
        "aktuell": letzter
    }


if __name__ == "__main__":

    print(luftdrucktrend_laden())