import requests

from config import LATITUDE, LONGITUDE
from cache import holen, speichern



def mond_laden():


    # ----------------------------------
    # Cache prüfen
    # ----------------------------------

    gespeichert = holen("mond")


    if gespeichert:

        print("CACHE MOND")

        return gespeichert





    url = (

        f"https://api.open-meteo.com/v1/forecast?"

        f"latitude={LATITUDE}"

        f"&longitude={LONGITUDE}"

        "&daily=moon_phase,sunrise,sunset"

        "&timezone=Europe/Berlin"

    )



    notfall_sonnenaufgang = "2026-01-01T08:00"

    notfall_sonnenuntergang = "2026-01-01T17:00"





    try:


        antwort = requests.get(

            url,

            timeout=10

        )


        daten = antwort.json()



    except Exception as e:


        print("MOND REQUEST FEHLER")

        print(e)



        return {


            "wert": 0,

            "name": "🌙 unbekannt",

            "alter": 0,

            "beleuchtung": 0,

            "bewertung": 0,

            "einfluss": "unbekannt",

            "beschreibung": "Monddaten aktuell nicht verfügbar",

            "sonnenaufgang": notfall_sonnenaufgang,

            "sonnenuntergang": notfall_sonnenuntergang

        }







    # ----------------------------------
    # API Fehler abfangen
    # ----------------------------------


    if "daily" not in daten:


        print("MOND API FEHLER")

        print(daten)



        return {


            "wert": 0,

            "name": "🌙 unbekannt",

            "alter": 0,

            "beleuchtung": 0,

            "bewertung": 0,

            "einfluss": "unbekannt",

            "beschreibung": "Monddaten aktuell nicht verfügbar",

            "sonnenaufgang": notfall_sonnenaufgang,

            "sonnenuntergang": notfall_sonnenuntergang

        }






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






    alter = round(

        phase * 29.53,

        1

    )





    beleuchtung = round(

        abs(0.5 - phase) * 200

    )






    if name in [

        "🌕 Vollmond",

        "🌔 zunehmender Mond"

    ]:


        bewertung = 8

        einfluss = "positiv"

        beschreibung = (

            "Helle Mondphasen können besonders nachts "
            "gute Aktivität fördern."

        )





    elif name in [

        "🌑 Neumond",

        "🌒 zunehmende Sichel"

    ]:


        bewertung = 7

        einfluss = "leicht positiv"

        beschreibung = (

            "Dunkle Nächte können vorsichtige Fische "
            "aktiver machen."

        )





    else:


        bewertung = 6

        einfluss = "leicht positiv"

        beschreibung = (

            "Abnehmender Mond kann weiterhin "
            "gute Nachtbedingungen bieten."

        )






    ergebnis = {


        "wert":

            phase,


        "name":

            name,


        "alter":

            alter,


        "beleuchtung":

            beleuchtung,


        "bewertung":

            bewertung,


        "einfluss":

            einfluss,


        "beschreibung":

            beschreibung,


        "sonnenaufgang":

            daten["daily"]["sunrise"][0],


        "sonnenuntergang":

            daten["daily"]["sunset"][0]

    }





    # ----------------------------------
    # Mond speichern
    # ----------------------------------

    speichern(

        "mond",

        ergebnis

    )



    print("MOND GESPEICHERT")



    return ergebnis