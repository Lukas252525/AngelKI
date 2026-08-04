from datetime import datetime



# --------------------------------------------------
# Uhrzeit simulieren
# --------------------------------------------------

def uhrzeit_setzen(stunde):


    jetzt = datetime.now()


    return jetzt.replace(
        hour=stunde,
        minute=0,
        second=0,
        microsecond=0
    )





# --------------------------------------------------
# Beste Prüfzeit je Fisch
# --------------------------------------------------

def beste_pruefzeit(fisch):


    if fisch == "Wels":

        return 23


    elif fisch == "Zander":

        return 22


    elif fisch == "Barsch":

        return 20


    elif fisch == "Hecht":

        return 7


    return 18





# --------------------------------------------------
# Aktivität mit Uhrzeit berechnen
# --------------------------------------------------

def berechne_prognose_aktivitaet(
    fisch,
    wetter,
    wasser
):


    # aktuelle Zeit sichern

    jetzt_alt = datetime.now()



    stunde = beste_pruefzeit(
        fisch
    )



    # --------------------------------------------------
    # Fischbewertung importieren
    # --------------------------------------------------

    from fisch_aktivitaet import berechne_fisch_aktivitaet



    # wir verändern die echte Zeit nicht,
    # sondern nutzen eine einfache Zeitbewertung


    punkte = 0

    gruende = []



    temperatur = wasser.get(
        "wassertemperatur",
        0
    )


    sauerstoff = wasser.get(
        "sauerstoff",
        0
    )


    truebung = wasser.get(
        "truebung",
        0
    )


    wolken = wetter.get(
        "cloud_cover",
        0
    )



    # ================================================
    # WELS
    # ================================================

    if fisch == "Wels":


        punkte += 30

        gruende.append(
            "Nachtphase optimal"
        )


        if temperatur >= 24:

            punkte += 20

            gruende.append(
                "warmes Wasser"
            )


        if sauerstoff >= 8:

            punkte += 10

            gruende.append(
                "guter Sauerstoff"
            )


        if truebung >= 5:

            punkte += 5

            gruende.append(
                "gute Trübung"
            )



    # ================================================
    # ZANDER
    # ================================================

    elif fisch == "Zander":


        punkte += 30

        gruende.append(
            "Dämmerung/Nacht"
        )


        if temperatur >= 20:

            punkte += 10

            gruende.append(
                "Sommerwasser"
            )


        if wolken >= 40:

            punkte += 15

            gruende.append(
                "Bewölkung unterstützt Jagd"
            )



    # ================================================
    # BARSCH
    # ================================================

    elif fisch == "Barsch":


        punkte += 25

        gruende.append(
            "Abendjagd"
        )


        if temperatur >= 20:

            punkte += 15

            gruende.append(
                "warme Temperaturen"
            )


        if truebung >= 5:

            punkte += 10

            gruende.append(
                "gute Jagdbedingungen"
            )



    # ================================================
    # HECHT
    # ================================================

    elif fisch == "Hecht":


        punkte += 30

        gruende.append(
            "Morgenphase"
        )


        if wolken >= 40:

            punkte += 15

            gruende.append(
                "Bewölkung hilft"
            )


        if temperatur < 25:

            punkte += 10

            gruende.append(
                "Temperatur passend"
            )


        else:

            punkte += 5

            gruende.append(
                "warmes Wasser"
            )



    if punkte > 100:

        punkte = 100



    return {

        "fisch":
            fisch,


        "prognose_punkte":
            punkte,


        "beste_stunde":
            stunde,


        "gruende":
            gruende

    }