NAME = "Wels"


def berechne(wetter, wasser, tageszeit, durchfluss):

    punkte = 50

    gruende = []

    phase = tageszeit["phase"]

    monat = int(wetter["datum"][5:7])


    methoden = {
        "Köderfisch auf Grund": 0,
        "Wurm auf Grund": 0
    }


    spots = {
        "Steinpackung": 0,
        "Tiefe Löcher": 0,
        "Flache Uferzone": 0,
        "Hafeneinfahrt": 0
    }



    # ----------------------------------
    # Jahreszeit
    # ----------------------------------

    if 5 <= monat <= 9:

        punkte += 3
        gruende.append("Warme Jahreszeit begünstigt Wels")


    elif 3 <= monat <= 4:

        punkte += 1
        gruende.append("Frühjahr beginnt")


    else:

        punkte -= 5
        gruende.append("Kalte Jahreszeit")



    # ----------------------------------
    # Wassertemperatur
    # ----------------------------------

    if wasser["wassertemperatur"] >= 24:

        punkte += 7
        gruende.append("Sehr gutes Welswasser")


    elif wasser["wassertemperatur"] >= 18:

        punkte += 4
        gruende.append("Gute Wassertemperatur")


    else:

        punkte -= 4
        gruende.append("Kaltes Wasser")



    # ----------------------------------
    # Sauerstoff
    # ----------------------------------

    if wasser["sauerstoff"] >= 8:

        punkte += 5
        gruende.append("Ausreichender Sauerstoff")



    # ----------------------------------
    # Durchfluss
    # ----------------------------------

    if 25 <= durchfluss["durchfluss"] <= 70:

        punkte += 10
        gruende.append("Ruhige Strömung")


    elif durchfluss["durchfluss"] < 25:

        punkte += 5
        gruende.append("Sehr ruhige Bedingungen")



    elif durchfluss["durchfluss"] > 100:

        punkte += 5
        gruende.append("Hoher Durchfluss aktiviert Fische")



    # ----------------------------------
    # Tageszeit
    # ----------------------------------

    if "Nacht" in phase:

        punkte += 14
        gruende.append("Starke Nachtaktivität")


    elif "Abend" in phase:

        punkte += 9
        gruende.append("Abendaktivität")


    elif "Morgen" in phase:

        punkte += 5
        gruende.append("Morgenaktivität")


    else:

        punkte -= 15
        gruende.append("Tageslicht reduziert Welsaktivität")



    # ----------------------------------
    # Methodenbewertung
    # ----------------------------------

    # Temperatur

    if wasser["wassertemperatur"] >= 24:

        methoden["Köderfisch auf Grund"] += 10
        methoden["Wurm auf Grund"] += 8


    elif wasser["wassertemperatur"] >= 18:

        methoden["Wurm auf Grund"] += 8
        methoden["Köderfisch auf Grund"] += 6



    # Tageszeit

    if "Nacht" in phase:

        methoden["Köderfisch auf Grund"] += 15
        methoden["Wurm auf Grund"] += 10


    elif "Abend" in phase:

        methoden["Wurm auf Grund"] += 10
        methoden["Köderfisch auf Grund"] += 8


    elif "Morgen" in phase:

        methoden["Wurm auf Grund"] += 5



    # Durchfluss

    if durchfluss["durchfluss"] < 45:

        methoden["Köderfisch auf Grund"] += 6
        methoden["Wurm auf Grund"] += 6


    elif durchfluss["durchfluss"] > 100:

        methoden["Köderfisch auf Grund"] += 8



    methode = max(methoden, key=methoden.get)



    # ----------------------------------
    # Spotbewertung
    # ----------------------------------

    if durchfluss["durchfluss"] < 45:

        spots["Tiefe Löcher"] += 12
        spots["Hafeneinfahrt"] += 8


    elif durchfluss["durchfluss"] > 100:

        spots["Steinpackung"] += 8



    if "Nacht" in phase:

        spots["Steinpackung"] += 12
        spots["Flache Uferzone"] += 8


    elif "Abend" in phase:

        spots["Steinpackung"] += 10
        spots["Hafeneinfahrt"] += 5


    elif "Morgen" in phase:

        spots["Tiefe Löcher"] += 6



    if wasser["wassertemperatur"] >= 24:

        spots["Flache Uferzone"] += 6
        spots["Steinpackung"] += 6


    elif wasser["wassertemperatur"] < 18:

        spots["Tiefe Löcher"] += 8



    spot = max(spots, key=spots.get)



    punkte = max(0, min(100, punkte))


    return {

        "fisch": NAME,

        "punkte": punkte,

        "gruende": gruende,

        "spot": spot,

        "methode": methode,

        "tiefe": "2-8 m",

        "methoden_ranking": sorted(
            methoden.items(),
            key=lambda x: x[1],
            reverse=True
        )

    }