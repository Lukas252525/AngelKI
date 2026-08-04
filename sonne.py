from datetime import datetime
from astral import LocationInfo
from astral.sun import sun



# Standort Mosel / Fankel
# gleiche Region wie deine Wetterdaten

BREITENGRAD = 49.95
LAENGENGRAD = 7.117



def sonnenzeiten_laden():


    heute = datetime.now()


    ort = LocationInfo(
        "Mosel",
        "Deutschland",
        "Europe/Berlin",
        BREITENGRAD,
        LAENGENGRAD
    )


    daten = sun(
        ort.observer,
        date=heute.date(),
        tzinfo=heute.astimezone().tzinfo
    )


    return {


        "sonnenaufgang":
            daten["sunrise"].strftime("%H:%M"),


        "sonnenuntergang":
            daten["sunset"].strftime("%H:%M"),


        "daemmerung_beginn":
            daten["sunset"].strftime("%H:%M")

    }



if __name__ == "__main__":


    ergebnis = sonnenzeiten_laden()


    print("===================")
    print("SONNEN TEST")
    print("===================")

    print(ergebnis)