import requests


URL = "https://geodaten-wasser.rlp-umwelt.de/api/data/gus_messwerte_messwerteaktuell?w=MESSST_NR=number:2691510700"


def finde(messung, *namen):
    """
    Sucht einen Wert unter mehreren möglichen Namen
    """

    for name in namen:

        if name in messung:
            return messung[name]

    return None



def wasser_laden():

    try:

        antwort = requests.get(
            URL,
            timeout=15
        )

        antwort.raise_for_status()

        daten = antwort.json()


        if not daten:
            raise Exception("Keine Wasserdaten erhalten")


        # API kann Liste oder Objekt liefern
        if isinstance(daten, list):

            messung = daten[0]

        elif isinstance(daten, dict):

            # falls API Features nutzt
            if "features" in daten:

                messung = daten["features"][0]["attributes"]

            else:

                messung = daten

        else:

            raise Exception("Unbekanntes API Format")



        return {


            "datum": finde(
                messung,
                "datum",
                "Datum"
            ),


            "uhrzeit": finde(
                messung,
                "uhrzeit",
                "Uhrzeit"
            ),


            "wassertemperatur": finde(
                messung,
                "wassertemperatur",
                "Wassertemperatur"
            ),


            "sauerstoff": finde(
                messung,
                "sauerstoff",
                "Sauerstoff"
            ),


            "ph": finde(
                messung,
                "ph",
                "pH",
                "pH_Wert"
            ),


            "leitfaehigkeit": finde(
                messung,
                "elektrische_leitfaehigkeit",
                "Elektrische Leitfähigkeit bei 25°C",
                "leitfaehigkeit"
            ),


            "truebung": finde(
                messung,
                "truebung",
                "Trübung"
            ),


            "nitrat": finde(
                messung,
                "nitrat",
                "Nitrat",
                "Nitrat-Stickstoff"
            ),


            "gesamtchlorophyll": finde(
                messung,
                "gesamtchlorophyll_a",
                "Gesamtchlorophyll a"
            ),


            "blaualgen": finde(
                messung,
                "blaualgenchlorophyll_a",
                "Blaualgenchlorophyll a"
            )

        }


    except Exception as e:


        return {

            "fehler": f"Wasser API Fehler: {e}"

        }