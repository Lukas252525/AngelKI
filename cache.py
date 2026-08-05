import time
import json
import os


DATEI = "cache.json"



def cache_laden():

    if not os.path.exists(DATEI):
        return {}

    try:

        with open(
            DATEI,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)


    except:

        return {}




def cache_speichern(cache):

    with open(
        DATEI,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            cache,
            f
        )




def holen(
    name,
    notfall=False
):

    cache = cache_laden()



    if name in cache:


        daten = cache[name]["daten"]

        zeit = cache[name]["zeit"]


        alter = time.time() - zeit



        # normaler Cache
        # 60 Minuten gültig

        if alter < 3600:

            return daten




        # Notfall Cache
        # bis 24 Stunden alt erlaubt

        if notfall and alter < 10800:

            return daten



    return None





def speichern(
    name,
    daten
):

    cache = cache_laden()



    cache[name] = {

        "daten": daten,

        "zeit": time.time()

    }



    cache_speichern(
        cache
    )