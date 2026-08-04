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



    # Mondalter berechnen
    alter = round(
        phase * 29.53,
        1
    )



    # Beleuchtung ungefähr berechnen
    beleuchtung = round(
        (1 - abs(phase - 0.5) * 2) * 100
    )



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





    # Einfluss auf Beißverhalten

    if phase < 0.0625 or phase >= 0.9375:

        bewertung = 5

        einfluss = "neutral"

        beschreibung = (
            "Neumond bringt wenig Mondlicht. "
            "Nachtaktive Fische orientieren sich stärker an anderen Faktoren."
        )



    elif phase < 0.5625:

        bewertung = 7

        einfluss = "leicht positiv"

        beschreibung = (
            "Zunehmender Mond kann die Aktivität "
            "in Dämmerung und Nacht unterstützen."
        )



    elif phase < 0.9375:

        bewertung = 6

        einfluss = "leicht positiv"

        beschreibung = (
            "Abnehmender Mond kann weiterhin gute "
            "Nachtbedingungen bieten."
        )



    else:

        bewertung = 5

        einfluss = "neutral"

        beschreibung = (
            "Mondphase hat aktuell nur geringen Einfluss."
        )





    return {


        "wert": phase,


        "name": name,


        "alter": alter,


        "beleuchtung": beleuchtung,


        "bewertung": bewertung,


        "einfluss": einfluss,


        "beschreibung": beschreibung,


        "sonnenaufgang":
            daten["daily"]["sunrise"][0],


        "sonnenuntergang":
            daten["daily"]["sunset"][0]

    }





if __name__ == "__main__":


    ergebnis = mond_laden()


    print("===================")

    print("MOND TEST")

    print("===================")

    print(ergebnis)