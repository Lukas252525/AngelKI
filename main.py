print("MAIN.PY WIRD GELADEN")


from wetter import wetter_laden
print("MAIN IMPORT OK")


from wasser import wasser_laden
from mond import mond_laden
from tageszeit import tageszeit_laden
from luftdruck import luftdrucktrend_laden
from pegel import pegel_laden
from durchfluss import durchfluss_laden


from beissindex import berechne_beissindex
from empfehlung import erstelle_empfehlung


from angelplanung import erstelle_angelplanung
from angelzeit_hilfe import zeit_bis_start



from wetter_trends import (

    erstelle_luftdruck_trend,

    erstelle_temperatur_trend,

    erstelle_bewoelkung_trend,

    erstelle_niederschlag_trend

)



from config import GEWAESSER







def angelki():


    print("ANGELKI START")



    # ----------------------------------
    # Wetter
    # ----------------------------------


    wetter = wetter_laden()


    print("WETTER GELADEN")



    wetter["luftdruck_trend"] = (

        erstelle_luftdruck_trend(wetter)

    )


    wetter["temperatur_trend"] = (

        erstelle_temperatur_trend(wetter)

    )


    wetter["bewoelkung_trend"] = (

        erstelle_bewoelkung_trend(wetter)

    )


    wetter["niederschlag_trend"] = (

        erstelle_niederschlag_trend(wetter)

    )







    # ----------------------------------
    # Wasser
    # ----------------------------------


    wasser = wasser_laden()



    print("WASSER TEST:")

    print(wasser)







    # ----------------------------------
    # Zusatzdaten
    # ----------------------------------


    mond = mond_laden()



    tageszeit = tageszeit_laden(

        mond

    )



    luftdruck = luftdrucktrend_laden()



    pegel = pegel_laden()



    durchfluss = durchfluss_laden()







    # ----------------------------------
    # Angelplanung
    # ----------------------------------


    angelplan = erstelle_angelplanung(

        wetter,

        wasser

    )





    beste_angelzeit = angelplan[0]





    startzeit = (

        beste_angelzeit["beste_zeit"]

        .split("-")[0]

        .strip()

    )





    beste_angelzeit["noch_bis"] = (

        zeit_bis_start(

            startzeit

        )

    )









    # ----------------------------------
    # Beißindex
    # ----------------------------------


    beissindex, kategorien = berechne_beissindex(

        wetter,

        wasser,

        mond,

        tageszeit,

        luftdruck,

        durchfluss,

        pegel

    )









    # ----------------------------------
    # Empfehlung
    # ----------------------------------


    empfehlung = erstelle_empfehlung(

        wetter,

        wasser,

        tageszeit,

        durchfluss

    )









    # ----------------------------------
    # Gesamtausgabe
    # ----------------------------------


    daten = {



        "gewaesser":

            GEWAESSER,





        "beissindex":

            beissindex,





        "kategorien":

            kategorien,





        "empfehlung":

            empfehlung,





        "angelplanung":

            {


                "beste_wahl":

                    beste_angelzeit,



                "alle_fische":

                    angelplan


            },







        "wetter":

            wetter,





        "wasser":

            wasser,





        "pegel":

            pegel,





        "durchfluss":

            durchfluss,





        "mond":

            mond



    }





    return daten











if __name__ == "__main__":



    ergebnis = angelki()



    print(ergebnis)