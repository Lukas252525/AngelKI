NAME = "Barsch"


def berechne(wetter, wasser, tageszeit, durchfluss):

    punkte = 50

    gruende = []

    phase = tageszeit["phase"]

    monat = int(wetter["datum"][5:7])


    methoden = {
        "Dropshot": 0,
        "Carolina Rig": 0,
        "Texas Rig": 0,
        "Kleiner Jig": 0,
        "Jigspinner": 0,
        "Spinner": 0,
        "Chatterbait": 0
    }


    spots = {
        "Steinpackung": 0,
        "Stege": 0,
        "Hafen": 0,
        "Hafeneinfahrt": 0,
        "Brücke": 0
    }


    farben = {
        "hell": 0,
        "dunkel": 0
    }

    kontraste = {
        "gering": 0,
        "hoch": 0
    }

    natuerlichkeit = {
        "natürlich": 0,
        "auffällig": 0
    }

    glitzer = {
        "kein": 0,
        "wenig": 0,
        "viel": 0
    }


    # ----------------------------------
    # Jahreszeit
    # ----------------------------------

    if 9 <= monat <= 10:
    
            punkte += 6
            gruende.append("Herbstphase")
    if 4 <= monat <= 5:
    
            punkte += 2
            gruende.append("Frühjahr")
    if 6 <= monat <= 8:

        punkte += 3
        gruende.append("Sommerphase")



    # ----------------------------------
    # Wassertemperatur
    # ----------------------------------

    if 18 <= wasser["wassertemperatur"] <= 23:

        punkte += 11
        gruende.append("Optimale Wassertemperatur")


    elif wasser["wassertemperatur"] <= 26:

        punkte += 7
        gruende.append("Gute Wassertemperatur")


    else:

        punkte -= 9
        gruende.append("Sehr warmes Wasser")



    # ----------------------------------
    # Sauerstoff
    # ----------------------------------

    if wasser["sauerstoff"] >= 10:

        punkte += 8
        gruende.append("Sehr hoher Sauerstoff")


    elif wasser["sauerstoff"] >= 8:

        punkte += 5
        gruende.append("Guter Sauerstoff")



    # ----------------------------------
    # Trübung
    # ----------------------------------

    if 8 <= wasser["truebung"] <= 18:

        punkte += 8
        gruende.append("Optimale Trübung")


    elif wasser["truebung"] <= 30:

        punkte += 4



    # ----------------------------------
    # Durchfluss
    # ----------------------------------

    if 40 <= durchfluss["durchfluss"] <= 120:

        punkte += 6
        gruende.append("Leichte Strömung")


    elif durchfluss["durchfluss"] < 40:

        punkte += 3
        gruende.append("Sehr geringer Durchfluss")



    # ----------------------------------
    # Tageszeit
    # ----------------------------------

    if "Abend" in phase:

        punkte += 12
        gruende.append("Abendbeißzeit")


    elif "Morgen" in phase:

        punkte += 10
        gruende.append("Morgenbeißzeit")


    elif "Nacht" in phase:

        punkte += 1


    else:

        punkte -= 8



    # ----------------------------------
    # Methodenbewertung
    # ----------------------------------

    if wasser["wassertemperatur"] >= 24:

        methoden["Dropshot"] += 10
        methoden["Carolina Rig"] += 8
        methoden["Texas Rig"] += 7


    elif wasser["wassertemperatur"] >= 18:

        methoden["Kleiner Jig"] += 8
        methoden["Spinner"] += 7



    if "Morgen" in phase:

        methoden["Spinner"] += 10
        methoden["Jigspinner"] += 8


    elif "Abend" in phase:

        methoden["Carolina Rig"] += 10
        methoden["Chatterbait"] += 8
        methoden["Jigspinner"] += 6
        methoden["Dropshot"] += 5


    elif "Nacht" in phase:

        methoden["Carolina Rig"] += 6



    if wasser["truebung"] < 12:

        methoden["Dropshot"] += 8
        methoden["Texas Rig"] += 6


    elif wasser["truebung"] < 25:

        methoden["Carolina Rig"] += 5
        methoden["Kleiner Jig"] += 4


    else:

        methoden["Chatterbait"] += 10
        methoden["Spinner"] += 8
        methoden["Jigspinner"] += 8



    if durchfluss["durchfluss"] < 45:

        methoden["Dropshot"] += 8
        methoden["Texas Rig"] += 5


    elif durchfluss["durchfluss"] > 100:

        methoden["Spinner"] += 6
        methoden["Jigspinner"] += 8



    if wetter["cloud_cover"] > 70:

        methoden["Chatterbait"] += 6
        methoden["Spinner"] += 4


    elif wetter["cloud_cover"] < 20:

        methoden["Dropshot"] += 4
        methoden["Texas Rig"] += 4



    methode = max(methoden, key=methoden.get)



    # ----------------------------------
    # Spotbewertung
    # ----------------------------------

    if durchfluss["durchfluss"] < 45:

        spots["Hafeneinfahrt"] += 12
        spots["Hafen"] += 8


    elif durchfluss["durchfluss"] > 100:

        spots["Steinpackung"] += 8



    if "Morgen" in phase:

        spots["Stege"] += 10
        spots["Steinpackung"] += 5


    elif "Abend" in phase:

        spots["Steinpackung"] += 12
        spots["Stege"] += 8


    elif "Nacht" in phase:

        spots["Steinpackung"] += 10



    if wasser["wassertemperatur"] >= 24:

        spots["Hafen"] += 6
        spots["Hafeneinfahrt"] += 6



    if wetter["cloud_cover"] < 20:

        spots["Brücke"] += 4



    if wasser["truebung"] > 20:

        spots["Hafen"] += 6



    spot = max(spots, key=spots.get)



    # ----------------------------------
    # Farbempfehlung
    # ----------------------------------

    if wasser["truebung"] < 8:

        farben["dunkel"] += 10
        kontraste["gering"] += 12
        natuerlichkeit["natürlich"] += 12
        glitzer["kein"] += 6
        glitzer["wenig"] += 8


    elif wasser["truebung"] < 15:

        farben["dunkel"] += 8
        kontraste["gering"] += 10
        natuerlichkeit["natürlich"] += 10
        glitzer["wenig"] += 8


    elif wasser["truebung"] < 25:

        farben["dunkel"] += 5
        farben["hell"] += 2
        kontraste["gering"] += 5
        kontraste["hoch"] += 3
        natuerlichkeit["natürlich"] += 8
        glitzer["wenig"] += 5


    else:

        farben["hell"] += 10
        kontraste["hoch"] += 12
        natuerlichkeit["auffällig"] += 10
        glitzer["viel"] += 10



    if wetter["cloud_cover"] < 20:

        farben["dunkel"] += 4
        natuerlichkeit["natürlich"] += 4
        glitzer["wenig"] += 3


    elif wetter["cloud_cover"] > 70:

        farben["hell"] += 6
        kontraste["hoch"] += 6
        glitzer["viel"] += 4



    if "Abend" in phase:

        farben["dunkel"] += 5
        kontraste["hoch"] += 4


    elif "Morgen" in phase:

        natuerlichkeit["natürlich"] += 3



    farbe = max(farben, key=farben.get)
    kontrast = max(kontraste, key=kontraste.get)
    natuerlich = max(natuerlichkeit, key=natuerlichkeit.get)
    glitzer_empfehlung = max(glitzer, key=glitzer.get)



    punkte = max(0, min(100, punkte))



    return {

        "fisch": NAME,

        "punkte": punkte,

        "gruende": gruende,

        "spot": spot,

        "methode": methode,

        "tiefe": "3-6 m",

        "farbe": farbe,

        "kontrast": kontrast,

        "natuerlichkeit": natuerlich,

        "glitzer": glitzer_empfehlung,

        "methoden_ranking": sorted(
            methoden.items(),
            key=lambda x: x[1],
            reverse=True
        )

    }