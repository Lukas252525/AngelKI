NAME = "Hecht"


def berechne(wetter, wasser, tageszeit, durchfluss):

    punkte = 50

    gruende = []

    phase = tageszeit["phase"]

    monat = int(wetter["datum"][5:7])


    methoden = {
        "Gummifisch": 0,
        "Wobbler": 0,
        "Jerkbait": 0,
        "Chatterbait": 0
    }


    spots = {
        "Steinpackung": 0,
        "Stege": 0,
        "Hafen": 0,
        "Hafeneinfahrt": 0,
        "Brücke": 0,
        "Flache Uferzone": 0
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

    if 3 <= monat <= 5:

        punkte += 6
        gruende.append("Frühjahrsphase")


    elif 6 <= monat <= 8:

        punkte -= 5
        gruende.append("Sommer reduziert Hechtaktivität")


    elif 9 <= monat <= 11:

        punkte += 8
        gruende.append("Herbstphase")



    # ----------------------------------
    # Wassertemperatur
    # ----------------------------------

    if 16 <= wasser["wassertemperatur"] <= 22:

        punkte += 11
        gruende.append("Optimale Hechttemperatur")


    elif wasser["wassertemperatur"] <= 24:

        punkte += 3
        gruende.append("Noch akzeptable Wassertemperatur")


    elif wasser["wassertemperatur"] <= 26:

        punkte -= 7
        gruende.append("Warme Wassertemperatur")


    else:

        punkte -= 12
        gruende.append("Sehr warmes Wasser")



    # ----------------------------------
    # Sauerstoff
    # ----------------------------------

    if wasser["sauerstoff"] >= 10:

        punkte += 6
        gruende.append("Hoher Sauerstoff")



    # ----------------------------------
    # Trübung
    # ----------------------------------

    if 10 <= wasser["truebung"] <= 25:

        punkte += 7
        gruende.append("Gute Raubfischtrübung")


    elif wasser["truebung"] > 30:

        punkte += 3



    # ----------------------------------
    # Durchfluss
    # ----------------------------------

    if durchfluss["durchfluss"] >= 50:

        punkte += 6
        gruende.append("Aktive Strömung")


    elif durchfluss["durchfluss"] < 45:

        punkte += 2
        gruende.append("Ruhige Bedingungen")



    # ----------------------------------
    # Tageszeit
    # ----------------------------------

    if "Morgen" in phase:

        punkte += 10
        gruende.append("Morgenaktivität")


    elif "Abend" in phase:

        punkte += 10
        gruende.append("Abendaktivität")


    elif "Nacht" in phase:

        punkte += 4
        gruende.append("Nachtaktivität")


    else:

        punkte -= 12
        gruende.append("Tageslicht erschwert Jagd")



    # ----------------------------------
    # Methodenbewertung
    # ----------------------------------

    # Temperatur

    if wasser["wassertemperatur"] >= 24:

        methoden["Gummifisch"] += 8
        methoden["Chatterbait"] += 8


    else:

        methoden["Wobbler"] += 8
        methoden["Jerkbait"] += 8



    # Tageszeit

    if "Morgen" in phase:

        methoden["Wobbler"] += 10
        methoden["Jerkbait"] += 8


    elif "Abend" in phase:

        methoden["Gummifisch"] += 10
        methoden["Chatterbait"] += 8


    elif "Nacht" in phase:

        methoden["Gummifisch"] += 6



    # Trübung

    if wasser["truebung"] < 15:

        methoden["Wobbler"] += 5
        methoden["Jerkbait"] += 5


    elif wasser["truebung"] < 25:

        methoden["Gummifisch"] += 6


    else:

        methoden["Chatterbait"] += 10
        methoden["Gummifisch"] += 8



    methode = max(methoden, key=methoden.get)



    # ----------------------------------
    # Spotbewertung
    # ----------------------------------

    if durchfluss["durchfluss"] < 45:

        spots["Hafen"] += 10
        spots["Hafeneinfahrt"] += 8


    else:

        spots["Steinpackung"] += 8



    if "Morgen" in phase:

        spots["Stege"] += 10
        spots["Brücke"] += 5


    elif "Abend" in phase:

        spots["Steinpackung"] += 12
        spots["Stege"] += 6


    elif "Nacht" in phase:

        spots["Flache Uferzone"] += 10
        spots["Steinpackung"] += 8



    if wasser["wassertemperatur"] >= 24:

        spots["Hafen"] += 6
        spots["Hafeneinfahrt"] += 6



    if wasser["truebung"] > 20:

        spots["Hafen"] += 5



    spot = max(spots, key=spots.get)



    # ----------------------------------
    # Farbempfehlung
    # ----------------------------------

    if wasser["truebung"] < 15:

        farben["hell"] += 6
        natuerlichkeit["natürlich"] += 10
        glitzer["wenig"] += 6


    elif wasser["truebung"] < 25:

        farben["hell"] += 8
        kontraste["hoch"] += 6
        natuerlichkeit["natürlich"] += 8


    else:

        farben["hell"] += 10
        kontraste["hoch"] += 12
        natuerlichkeit["auffällig"] += 10
        glitzer["viel"] += 10



    if wetter["cloud_cover"] < 20:

        natuerlichkeit["natürlich"] += 4


    elif wetter["cloud_cover"] > 70:

        kontraste["hoch"] += 5
        glitzer["viel"] += 4



    if "Abend" in phase:

        kontraste["hoch"] += 5


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

        "tiefe": "1-5 m",

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