import requests


URL = "https://geodaten-wasser.rlp-umwelt.de/api/data/gus_messwerte_messwerteaktuell?w=MESSST_NR=number:2691510700"


def wasser_laden():

    try:

        antwort = requests.get(
            URL,
            timeout=15
        )

        daten = antwort.json()


        # Debug falls Format anders ist
        if not daten:
            raise Exception("Keine Wasserdaten erhalten")


        # erste Messung nehmen
        messung = daten[0]


        return {

            "datum": messung.get("datum", ""),
            "uhrzeit": messung.get("uhrzeit", ""),

            "wassertemperatur": messung.get("wassertemperatur"),
            "sauerstoff": messung.get("sauerstoff"),
            "ph": messung.get("ph"),

            "leitfaehigkeit": messung.get(
                "elektrische_leitfaehigkeit"
            ),

            "truebung": messung.get("truebung"),

            "nitrat": messung.get("nitrat"),

            "gesamtchlorophyll": messung.get(
                "gesamtchlorophyll_a"
            ),

            "blaualgen": messung.get(
                "blaualgenchlorophyll_a"
            )

        }


    except Exception as e:

        return {
            "fehler": f"Wasser API Fehler: {e}"
        }