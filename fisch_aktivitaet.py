from datetime import datetime



# --------------------------------------------------
# Fischspezifische Aktivitätsbewertung
# --------------------------------------------------

def berechne_fisch_aktivitaet(
    fisch,
    wetter,
    wasser
):


    jetzt = datetime.now()

    stunde = jetzt.hour



    punkte = 0

    gruende = []



    # -----------------------------
    # Wasserwerte
    # -----------------------------

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



    # -----------------------------
    # Wetterwerte
    # -----------------------------

    wolken = wetter.get(
        "cloud_cover",
        0
    )


    druck_trend = wetter.get(
        "luftdruck_trend",
        {}
    )



    # ==================================================
    # WELS
    # ==================================================

    if fisch == "Wels":


        # Tageszeit

        if stunde >= 21 or stunde < 6:


            punkte += 30


            gruende.append(
                "Nachtphase optimal für Wels"
            )


        elif stunde >= 18:


            punkte += 15


            gruende.append(
                "Abendphase nähert sich"
            )


        else:


            punkte += 5


            gruende.append(
                "Wels wird meist später aktiv"
            )



        # Temperatur

        if temperatur >= 24:


            punkte += 20


            gruende.append(
                "Warmes Wasser begünstigt Wels"
            )


        elif temperatur >= 18:


            punkte += 10


            gruende.append(
                "geeignete Wassertemperatur"
            )



        # Sauerstoff

        if sauerstoff >= 8:


            punkte += 10


            gruende.append(
                "Guter Sauerstoffgehalt"
            )



        # Trübung

        if truebung >= 5:


            punkte += 5


            gruende.append(
                "Gute Trübung für Wels"
            )



    # ==================================================
    # ZANDER
    # ==================================================

    elif fisch == "Zander":



        if stunde >= 20 or stunde < 1:


            punkte += 30


            gruende.append(
                "Dämmerung/Nacht erhöht Zanderaktivität"
            )


        elif stunde >= 17:


            punkte += 15


            gruende.append(
                "Abendphase nähert sich"
            )


        else:


            punkte += 5


            gruende.append(
                "Tageslicht reduziert Zanderaktivität"
            )



        if temperatur >= 20:


            punkte += 10


            gruende.append(
                "Sommerwasser passt"
            )



        if wolken >= 50:


            punkte += 15


            gruende.append(
                "Bewölkung unterstützt Zanderjagd"
            )



        if druck_trend:


            differenz = (

                druck_trend["wert_24h"]

                -

                druck_trend["jetzt"]

            )


            if abs(differenz) <= 2:


                punkte += 10


                gruende.append(
                    "Stabiler Luftdruck"
                )



    # ==================================================
    # BARSCH
    # ==================================================

    elif fisch == "Barsch":



        if 17 <= stunde <= 22:


            punkte += 25


            gruende.append(
                "Abendphase erhöht Barschaktivität"
            )


        elif 5 <= stunde <= 9:


            punkte += 20


            gruende.append(
                "Morgenphase aktiv"
            )


        else:


            punkte += 5


            gruende.append(
                "Ruhephase"
            )



        if temperatur >= 20:


            punkte += 15


            gruende.append(
                "Warme Temperaturen"
            )



        if truebung >= 5:


            punkte += 10


            gruende.append(
                "Gute Jagdbedingungen"
            )



        if druck_trend:


            differenz = (

                druck_trend["wert_24h"]

                -

                druck_trend["jetzt"]

            )


            if abs(differenz) <= 2:


                punkte += 5


                gruende.append(
                    "Stabile Wetterlage"
                )



    # ==================================================
    # HECHT
    # ==================================================

    elif fisch == "Hecht":



        if 5 <= stunde <= 9:


            punkte += 30


            gruende.append(
                "Morgenjagd"
            )


        elif 17 <= stunde <= 20:


            punkte += 20


            gruende.append(
                "Abendaktivität"
            )


        else:


            punkte += 5


            gruende.append(
                "Außerhalb Hauptzeit"
            )



        if wolken >= 40:


            punkte += 15


            gruende.append(
                "Bewölkung verbessert Jagdbedingungen"
            )



        if temperatur < 25:


            punkte += 10


            gruende.append(
                "Angenehme Wassertemperatur"
            )


        else:


            punkte += 5


            gruende.append(
                "Sehr warmes Wasser reduziert Hechtaktivität"
            )



    # Begrenzung

    if punkte > 100:

        punkte = 100



    return {


        "punkte":
            punkte,


        "gruende":
            gruende

    }