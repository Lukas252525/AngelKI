import requests


URL = (
    "https://geodaten-wasser.rlp-umwelt.de/"
    "api/data/gus_messwerte_messwerteaktuell"
    "?w=MESSST_NR=number:2691510700"
)


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "Chrome/120 Safari/537.36"
    ),
    "Referer": "https://geodaten-wasser.rlp-umwelt.de/"
}



def wasser_laden():

    try:

        antwort = requests.get(
            URL,
            headers=HEADERS,
            timeout=15
        )

        antwort.raise_for_status()

        daten = antwort.json()


        if not daten:
            raise Exception(
                "Keine Wasserdaten erhalten"
            )


        # Grunddaten vom ersten Eintrag
        datum = daten[0].get(
            "datum",
            ""
        )

        uhrzeit = daten[0].get(
            "uhrzeit",
            ""
        )


        werte = {}


        # Alle Messwerte durchgehen

        for eintrag in daten:

            name = eintrag.get(
                "stoff_bezeichnung",
                ""
            )

            wert = eintrag.get(
                "messwert",
                0
            )


            werte[name] = wert



        return {


            "datum": datum,

            "uhrzeit": uhrzeit,


            "wassertemperatur":
                werte.get(
                    "Wassertemperatur",
                    0
                ),


            "sauerstoff":
                werte.get(
                    "Sauerstoff",
                    0
                ),


            "ph":
                werte.get(
                    "pH-Wert",
                    0
                ),


            "leitfaehigkeit":
                werte.get(
                    "Elektrische Leitfähigkeit bei 25°C",
                    0
                ),


            "truebung":
                werte.get(
                    "Trübung",
                    0
                ),


            "nitrat":
                werte.get(
                    "Nitrat-Stickstoff",
                    0
                ),


            "gesamtchlorophyll":
                werte.get(
                    "Gesamtchlorophyll a",
                    0
                ),


            "blaualgen":
                werte.get(
                    "Blaualgenchlorophyll a",
                    0
                )

        }



    except Exception as e:


        print("WASSER FEHLER:")
        print(e)


        return {

            "datum": "",
            "uhrzeit": "",

            "wassertemperatur": 0,
            "sauerstoff": 0,
            "ph": 0,
            "leitfaehigkeit": 0,
            "truebung": 0,
            "nitrat": 0,
            "gesamtchlorophyll": 0,
            "blaualgen": 0

        }