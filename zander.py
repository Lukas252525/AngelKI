NAME = "Zander"


def berechne(wetter, wasser, tageszeit, durchfluss):

    punkte = 50

    gruende = []

    phase = tageszeit["phase"]

    monat = int(wetter["datum"][5:7])


    methoden = {
        "Gummifisch": 0,
        "Carolina Rig mit Creature Bait": 0,
        "Köderfisch auf Grund": 0,
        "Dropshot": 0,
        "Flachlaufender Wobbler": 0
    }


    spots = {
        "Steinpackung": 0,
        "Hafeneinfahrt": 0,
        "Flache Uferzone": 0,
        "Brücke": 0,
        "Tiefe Löcher": 0
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

        punkte += 0
        gruende.append("Sommerphase")



    if 6 <= monat <= 8 and "Nacht" in phase:

        punkte += 3
        gruende.append("Sommernacht erhöht Zanderaktivität")



    # ----------------------------------
    # Wassertemperatur
    # ----------------------------------

    if 16 <= wasser["wassertemperatur"] <= 22:

        punkte += 11
        gruende.append("Optimale Zandertemperatur")


    elif wasser["wassertemperatur"] <= 25:

        punkte += 4
        gruende.append("Noch gute Wassertemperatur")


    else:

        punkte -= 10
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

        punkte += 8
        gruende.append("Passende Räubertrübung")


    elif wasser["truebung"] <= 35:

        punkte += 3



    # ----------------------------------
    # Durchfluss
    # ----------------------------------

    if 50 <= durchfluss["durchfluss"] <= 150:

        punkte += 8
        gruende.append("Guter Durchfluss")


    elif 35 <= durchfluss["durchfluss"] < 50:

        punkte += 4
        gruende.append("Geringer Durchfluss")



    # ----------------------------------
    # Tageszeit
    # ----------------------------------

    if "Nacht" in phase:

        punkte += 18
        gruende.append("Starke Nachtaktivität")


    elif "Abend" in phase:

        punkte += 11
        gruende.append("Abendbeißzeit")


    elif "Morgen" in phase:

        punkte += 5
        gruende.append("Morgenaktivität")


    else:

        punkte -= 18
        gruende.append("Tageslicht reduziert Zanderaktivität")



    # ----------------------------------
    # Methodenbewertung
    # ----------------------------------

    # Temperatur

    if wasser["wassertemperatur"] >= 24:

        methoden["Dropshot"] += 8
        methoden["Carolina Rig mit Creature Bait"] += 8
        methoden["Köderfisch auf Grund"] += 6


    elif wasser["wassertemperatur"] < 24:

        methoden["Gummifisch"] += 8
        methoden["Flachlaufender Wobbler"] += 6



    # Tageszeit

    if "Abend" in phase:

        methoden["Gummifisch"] += 10
        methoden["Dropshot"] += 6


    elif "Nacht" in phase:

        methoden["Flachlaufender Wobbler"] += 14
        methoden["Köderfisch auf Grund"] += 12


    elif "Morgen" in phase:

        methoden["Gummifisch"] += 6



    # Trübung

    if wasser["truebung"] < 12:

        methoden["Dropshot"] += 6
        methoden["Carolina Rig mit Creature Bait"] += 5


    elif wasser["truebung"] < 25:

        methoden["Gummifisch"] += 8


    else:

        methoden["Gummifisch"] += 10
        methoden["Flachlaufender Wobbler"] += 6



    # Durchfluss

    if durchfluss["durchfluss"] < 45:

        methoden["Dropshot"] += 6
        methoden["Carolina Rig mit Creature Bait"] += 5


    elif durchfluss["durchfluss"] > 100:

        methoden["Gummifisch"] += 6



    methode = max(methoden, key=methoden.get)



    # ----------------------------------
    # Spotbewertung
    # ----------------------------------

    if durchfluss["durchfluss"] < 45:

        spots["Hafeneinfahrt"] += 12
        spots["Tiefe Löcher"] += 8


    elif durchfluss["durchfluss"] > 100:

        spots["Steinpackung"] += 8



    if "Abend" in phase:

        spots["Steinpackung"] += 12
        spots["Hafeneinfahrt"] += 6


    elif "Nacht" in phase:

        spots["Flache Uferzone"] += 15
        spots["Steinpackung"] += 8


    elif "Morgen" in phase:

        spots["Brücke"] += 6



    if wasser["wassertemperatur"] >= 24:

        spots["Tiefe Löcher"] += 10



    if wetter["cloud_cover"] < 20:

        spots["Brücke"] += 4



    if wasser["truebung"] > 20:

        spots["Steinpackung"] += 6
        spots["Hafeneinfahrt"] += 4



    spot = max(spots, key=spots.get)



    # ----------------------------------
    # Farbempfehlung
    # ----------------------------------

    if wasser["truebung"] < 8:

        farben["dunkel"] += 10
        kontraste["gering"] += 8
        natuerlichkeit["natürlich"] += 12
        glitzer["kein"] += 6
        glitzer["wenig"] += 8


    elif wasser["truebung"] < 15:

        farben["dunkel"] += 8
        kontraste["gering"] += 6
        natuerlichkeit["natürlich"] += 10
        glitzer["wenig"] += 8


    elif wasser["truebung"] < 25:

        farben["dunkel"] += 5
        farben["hell"] += 3
        kontraste["hoch"] += 6
        natuerlichkeit["natürlich"] += 8
        glitzer["wenig"] += 5


    else:

        farben["hell"] += 10
        kontraste["hoch"] += 12
        natuerlichkeit["auffällig"] += 10
        glitzer["viel"] += 10



    if wetter["cloud_cover"] > 70:

        kontraste["hoch"] += 5
        glitzer["viel"] += 4


    elif wetter["cloud_cover"] < 20:

        farben["dunkel"] += 4
        natuerlichkeit["natürlich"] += 4



    if "Abend" in phase:

        farben["dunkel"] += 5
        kontraste["hoch"] += 6


    elif "Nacht" in phase:

        farben["dunkel"] += 8
        kontraste["hoch"] += 10
        glitzer["kein"] += 6



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

        "tiefe": "4-7 m",

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