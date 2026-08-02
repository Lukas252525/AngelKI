from wetter import wetter_laden
from wasser import wasser_laden
from mond import mond_laden
from tageszeit import tageszeit_laden
from luftdruck import luftdrucktrend_laden
from pegel import pegel_laden
from durchfluss import durchfluss_laden

from beissindex import berechne_beissindex
from empfehlung import erstelle_empfehlung

from config import GEWAESSER


def angelki():

    wetter = wetter_laden()
    wasser = wasser_laden()
    mond = mond_laden()

    tageszeit = tageszeit_laden(mond)

    luftdruck = luftdrucktrend_laden()

    pegel = pegel_laden()

    durchfluss = durchfluss_laden()


    beissindex, kategorien = berechne_beissindex(
        wetter,
        wasser,
        mond,
        tageszeit,
        luftdruck,
        durchfluss,
        pegel
    )


    empfehlung = erstelle_empfehlung(
        wetter,
        wasser,
        tageszeit,
        durchfluss
    )


    daten = {

        "gewaesser": GEWAESSER,

        "beissindex": beissindex,

        "kategorien": kategorien,

        "empfehlung": empfehlung,

        "wetter": wetter,

        "wasser": wasser

    }


    return daten



if __name__ == "__main__":

    ergebnis = angelki()

    print(ergebnis)