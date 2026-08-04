from angelprognose import berechne_prognose_aktivitaet
from sonne import sonnenzeiten_laden

from datetime import datetime, timedelta




# --------------------------------------------------
# Uhrzeit rechnen
# --------------------------------------------------

def zeit_minus(
    zeit,
    minuten
):

    uhrzeit = datetime.strptime(
        zeit,
        "%H:%M"
    )


    neu = uhrzeit - timedelta(
        minutes=minuten
    )


    return neu.strftime(
        "%H:%M"
    )





def zeit_plus(
    zeit,
    minuten
):

    uhrzeit = datetime.strptime(
        zeit,
        "%H:%M"
    )


    neu = uhrzeit + timedelta(
        minutes=minuten
    )


    return neu.strftime(
        "%H:%M"
    )





# --------------------------------------------------
# Zeitfenster je Fisch
# --------------------------------------------------

def zeitfenster_fisch(
    fisch,
    sonne
):


    aufgang = sonne[
        "sonnenaufgang"
    ]


    untergang = sonne[
        "sonnenuntergang"
    ]



    if fisch == "Wels":


        return {


            "zeit":
                (
                    zeit_plus(
                        untergang,
                        60
                    )
                    +
                    " - "
                    +
                    aufgang
                ),


            "beschreibung":
                "Nachtphase nach Sonnenuntergang"

        }




    elif fisch == "Zander":


        return {


            "zeit":
                (
                    untergang
                    +
                    " - 00:30"
                ),


            "beschreibung":
                "Dämmerung und frühe Nacht"

        }




    elif fisch == "Barsch":


        return {


            "zeit":
                (
                    zeit_minus(
                        untergang,
                        120
                    )
                    +
                    " - "
                    +
                    zeit_plus(
                        untergang,
                        30
                    )
                ),


            "beschreibung":
                "Abendaktivität"

        }




    elif fisch == "Hecht":


        return {


            "zeit":
                (
                    aufgang
                    +
                    " - "
                    +
                    zeit_plus(
                        aufgang,
                        120
                    )
                ),


            "beschreibung":
                "Morgenjagd"

        }




    return {


        "zeit":
            "unbekannt",


        "beschreibung":
            "keine Daten"

    }





# --------------------------------------------------
# Angelplanung erstellen
# --------------------------------------------------

def erstelle_angelplanung(
    wetter,
    wasser
):


    sonne = sonnenzeiten_laden()



    fische = [

        "Wels",
        "Zander",
        "Barsch",
        "Hecht"

    ]



    plan = []



    for fisch in fische:


        prognose = berechne_prognose_aktivitaet(

            fisch,

            wetter,

            wasser

        )


        zeit = zeitfenster_fisch(

            fisch,

            sonne

        )



        plan.append({

            "fisch":
                fisch,


            "aktivitaet":
                prognose["prognose_punkte"],


            "beste_zeit":
                zeit["zeit"],


            "beschreibung":
                zeit["beschreibung"],


            "gruende":
                prognose["gruende"]

        })



    plan.sort(

        key=lambda x:
            x["aktivitaet"],

        reverse=True

    )


    return plan