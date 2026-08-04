def finde_aktuellen_index(wetter):

    zeiten = wetter["hourly_time"]

    aktuelle_uhrzeit = wetter["uhrzeit"]


    for i, zeit in enumerate(zeiten):

        if zeit[11:16] == aktuelle_uhrzeit:

            return i


    return 0





# ----------------------------------
# Luftdrucktrend 24h
# ----------------------------------

def erstelle_luftdruck_trend(wetter):


    druck = wetter["hourly_pressure"]

    zeiten = wetter["hourly_time"]


    index_jetzt = finde_aktuellen_index(
        wetter
    )


    jetzt = druck[index_jetzt]


    index_24h = min(
        index_jetzt + 24,
        len(druck)-1
    )


    wert_24h = druck[index_24h]


    return {

        "jetzt": jetzt,

        "wert_24h": wert_24h,

        "zeit_24h": zeiten[index_24h]

    }





# ----------------------------------
# Temperaturtrend 24h
# ----------------------------------

def erstelle_temperatur_trend(wetter):


    temperatur = wetter["hourly_temperature"]

    zeiten = wetter["hourly_time"]


    index_jetzt = finde_aktuellen_index(
        wetter
    )


    jetzt = temperatur[index_jetzt]


    index_24h = min(
        index_jetzt + 24,
        len(temperatur)-1
    )


    wert_24h = temperatur[index_24h]


    return {

        "jetzt": jetzt,

        "wert_24h": wert_24h,

        "zeit_24h": zeiten[index_24h]

    }





# ----------------------------------
# Bewölkungstrend 6h
# ----------------------------------

def erstelle_bewoelkung_trend(wetter):


    wolken = wetter["hourly_cloud"]

    zeiten = wetter["hourly_time"]


    index_jetzt = finde_aktuellen_index(
        wetter
    )


    jetzt = wolken[index_jetzt]


    index_6h = min(
        index_jetzt + 6,
        len(wolken)-1
    )


    wert_6h = wolken[index_6h]


    return {

        "jetzt": jetzt,

        "wert_6h": wert_6h,

        "zeit_6h": zeiten[index_6h]

    }





# ----------------------------------
# Niederschlagstrend 6h
# ----------------------------------

def erstelle_niederschlag_trend(wetter):


    regen = wetter["hourly_precipitation"]

    zeiten = wetter["hourly_time"]


    index_jetzt = finde_aktuellen_index(
        wetter
    )


    index_ende = min(
        index_jetzt + 6,
        len(regen)
    )


    menge = 0


    for wert in regen[index_jetzt:index_ende]:

        menge += wert



    return {

        "menge": round(
            menge,
            1
        ),

        "zeit_6h": zeiten[index_ende-1]

    }