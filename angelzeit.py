from datetime import datetime, timedelta

from sonne import sonnenzeiten_laden




# --------------------------------------------------
# Tagesphase
# --------------------------------------------------

def berechne_tagesphase():


    jetzt = datetime.now()

    stunde = jetzt.hour



    if 5 <= stunde < 9:

        phase = "Morgen"


    elif 9 <= stunde < 17:

        phase = "Tag"


    elif 17 <= stunde < 21:

        phase = "Abend"


    elif 21 <= stunde < 24:

        phase = "Dämmerung/Nacht"


    else:

        phase = "Nacht"



    return {

        "phase": phase,

        "zeit": jetzt,

        "uhrzeit":
            jetzt.strftime("%H:%M")

    }





# --------------------------------------------------
# Wasser Einfluss
# --------------------------------------------------

def wasser_bewertung(wasser):


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


    blaualgen = wasser.get(
        "blaualgen",
        0
    )



    if temperatur >= 24:

        punkte += 5

        gruende.append(
            "warmes Wasser"
        )


    elif 18 <= temperatur < 24:

        punkte += 3

        gruende.append(
            "gute Wassertemperatur"
        )



    if sauerstoff >= 8:

        punkte += 5

        gruende.append(
            "guter Sauerstoff"
        )


    elif sauerstoff < 5:

        punkte -= 5

        gruende.append(
            "wenig Sauerstoff"
        )



    if 5 <= truebung <= 20:

        punkte += 3

        gruende.append(
            "gute Trübung"
        )



    if blaualgen < 20:

        punkte += 2

        gruende.append(
            "kaum Blaualgen"
        )



    return punkte, gruende





# --------------------------------------------------
# Wetter Einfluss
# --------------------------------------------------

def wetter_bewertung(wetter):


    punkte = 0

    gruende = []



    temp = wetter.get(
        "temperatur_trend",
        {}
    )


    druck = wetter.get(
        "luftdruck_trend",
        {}
    )


    wolken = wetter.get(
        "bewoelkung_trend",
        {}
    )


    regen = wetter.get(
        "niederschlag_trend",
        {}
    )



    # Temperaturtrend

    if temp:


        differenz = (
            temp["wert_24h"]
            -
            temp["jetzt"]
        )


        if differenz <= -3:

            punkte += 5

            gruende.append(
                "Abkühlung nach warmer Phase"
            )


        elif abs(differenz) <= 1:

            punkte += 2

            gruende.append(
                "stabile Temperatur"
            )



    # Luftdruck

    if druck:


        differenz = (
            druck["wert_24h"]
            -
            druck["jetzt"]
        )


        if abs(differenz) <= 2:

            punkte += 4

            gruende.append(
                "stabiler Luftdruck"
            )


        elif abs(differenz) <= 5:

            punkte += 2

            gruende.append(
                "leichte Luftdruckänderung"
            )



    # Bewölkung

    if wolken:


        unterschied = (
            wolken["wert_6h"]
            -
            wolken["jetzt"]
        )


        if unterschied >= 20:

            punkte += 4

            gruende.append(
                "Bewölkung nimmt zu"
            )


        elif abs(unterschied) < 10:

            punkte += 2

            gruende.append(
                "Bewölkung stabil"
            )



    # Regen

    if regen:


        menge = regen.get(
            "menge",
            0
        )


        if 0 < menge <= 2:

            punkte += 2

            gruende.append(
                "leichter Regen möglich"
            )


        elif menge == 0:

            punkte += 1

            gruende.append(
                "trocken"
            )



    return punkte, gruende





# --------------------------------------------------
# Fischabhängige Zeiten
# --------------------------------------------------

def fisch_beisszeit(
    fisch,
    sonne
):


    aufgang = datetime.strptime(
        sonne["sonnenaufgang"],
        "%H:%M"
    )


    untergang = datetime.strptime(
        sonne["sonnenuntergang"],
        "%H:%M"
    )



    if fisch == "Wels":


        return {

            "start":
                untergang + timedelta(hours=1),

            "ende":
                aufgang,

            "beschreibung":
                "Nacht nach Sonnenuntergang"

        }



    elif fisch == "Zander":


        return {

            "start":
                untergang,

            "ende":
                datetime.strptime(
                    "00:00",
                    "%H:%M"
                ),

            "beschreibung":
                "Dämmerung und Nacht"

        }



    elif fisch == "Barsch":


        return {

            "start":
                untergang - timedelta(hours=2),

            "ende":
                untergang + timedelta(minutes=30),

            "beschreibung":
                "Abendjagd"

        }



    elif fisch == "Hecht":


        return {

            "start":
                aufgang,

            "ende":
                aufgang + timedelta(hours=2),

            "beschreibung":
                "Morgenaktivität"

        }



# --------------------------------------------------
# Countdown
# --------------------------------------------------

def countdown(start):


    jetzt = datetime.now()


    ziel = start.replace(
        year=jetzt.year,
        month=jetzt.month,
        day=jetzt.day
    )


    if ziel < jetzt:

        ziel += timedelta(
            days=1
        )


    sekunden = (
        ziel - jetzt
    ).total_seconds()



    stunden = int(
        sekunden // 3600
    )


    minuten = int(
        (sekunden % 3600)//60
    )


    return f"{stunden}h {minuten}min"





# --------------------------------------------------
# Hauptfunktion
# --------------------------------------------------

def berechne_angelzeit(
    wetter,
    wasser,
    empfehlung
):


    tageszeit = berechne_tagesphase()


    sonne = sonnenzeiten_laden()


    fisch = empfehlung["fisch"]



    aktivitaet = 40


    gruende = []



    wasserpunkte, wassergruende = wasser_bewertung(
        wasser
    )


    aktivitaet += wasserpunkte

    gruende.extend(
        wassergruende
    )



    wetterpunkte, wettergruende = wetter_bewertung(
        wetter
    )


    aktivitaet += wetterpunkte

    gruende.extend(
        wettergruende
    )



    beisszeit = fisch_beisszeit(
        fisch,
        sonne
    )


    start = beisszeit["start"]

    ende = beisszeit["ende"]



    jetzt = datetime.now()



    if start <= jetzt <= ende:


        aktivitaet += 20

        status = "Beste Phase läuft"


        gruende.append(
            "Aktuelle Uhrzeit liegt in der Beißphase"
        )


    else:


        status = "Warten bis zur Hauptphase"


        gruende.append(
            "Hauptphase kommt später"
        )



    if aktivitaet > 100:

        aktivitaet = 100



    return {


        "fisch":
            fisch,


        "aktuelle_uhrzeit":
            tageszeit["uhrzeit"],


        "phase":
            tageszeit["phase"],


        "aktivitaet":
            aktivitaet,


        "status":
            status,


        "beste_zeit":
            (
                start.strftime("%H:%M")
                +
                " - "
                +
                ende.strftime("%H:%M")
            ),


        "beschreibung":
            beisszeit["beschreibung"],


        "noch_bis":
            countdown(start),


        "sonnenzeiten":
            sonne,


        "gruende":
            gruende

    }