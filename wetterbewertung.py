def bewerte_wetterprognose(wetter):

    punkte = 0
    max_punkte = 10

    gruende = []


    # ----------------------------------
    # Temperaturtrend (max. 3 Punkte)
    # ----------------------------------

    temp = wetter["temperatur_trend"]

    differenz_temp = round(
        temp["wert_24h"] - temp["jetzt"],
        1
    )


    if differenz_temp <= -5:

        punkte += 3
        gruende.append(
            "Starke Abkühlung erwartet"
        )

    elif differenz_temp <= -2:

        punkte += 2
        gruende.append(
            "Abkühlung erwartet"
        )

    elif abs(differenz_temp) <= 1:

        punkte += 1
        gruende.append(
            "Temperatur bleibt stabil"
        )

    else:

        gruende.append(
            "Weitere Erwärmung erwartet"
        )



    # ----------------------------------
    # Bewölkung (max. 3 Punkte)
    # ----------------------------------

    wolken = wetter["bewoelkung_trend"]


    differenz_wolken = (
        wolken["wert_6h"]
        -
        wolken["jetzt"]
    )


    if differenz_wolken >= 30:

        punkte += 3
        gruende.append(
            "Bewölkung nimmt deutlich zu"
        )

    elif differenz_wolken >= 10:

        punkte += 2
        gruende.append(
            "Mehr Bewölkung erwartet"
        )

    elif abs(differenz_wolken) < 10:

        punkte += 1
        gruende.append(
            "Bewölkung bleibt ähnlich"
        )

    else:

        gruende.append(
            "Himmel klart auf"
        )



    # ----------------------------------
    # Luftdruck (max. 2 Punkte)
    # ----------------------------------

    druck = wetter["luftdruck_trend"]


    differenz_druck = round(
        druck["wert_24h"]
        -
        druck["jetzt"],
        1
    )


    if abs(differenz_druck) <= 2:

        punkte += 2
        gruende.append(
            "Luftdruck stabil"
        )

    elif abs(differenz_druck) <= 5:

        punkte += 1
        gruende.append(
            "Leichte Luftdruckänderung"
        )

    else:

        gruende.append(
            "Starke Luftdruckänderung"
        )



    # ----------------------------------
    # Niederschlag (max. 2 Punkte)
    # ----------------------------------

    regen = wetter["niederschlag_trend"]["menge"]


    if 0 < regen <= 2:

        punkte += 2
        gruende.append(
            "Leichter Regen möglich"
        )

    elif regen == 0:

        punkte += 1
        gruende.append(
            "Trockenes Wetter"
        )

    else:

        gruende.append(
            "Stärkerer Regen erwartet"
        )



    return {

        "punkte": punkte,

        "max": max_punkte,

        "gruende": gruende

    }