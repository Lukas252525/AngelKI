from bewertung import (
    bewerte_jahreszeit,
    bewerte_wetter,
    bewerte_wasser,
    bewerte_hydrologie,
    bewerte_tageszeit,
    bewerte_mond
)


def berechne_beissindex(
    wetter,
    wasser,
    mond,
    tageszeit,
    luftdruck,
    durchfluss,
    pegel
):

    kategorien = {}

    # ----------------------------------------------------------
    # Jahreszeit
    # ----------------------------------------------------------

    punkte, gruende = bewerte_jahreszeit(wetter)

    kategorien["Jahreszeit"] = {
        "punkte": punkte,
        "max": 15,
        "gruende": gruende
    }

    # ----------------------------------------------------------
    # Wetter
    # ----------------------------------------------------------

    punkte, gruende = bewerte_wetter(
        wetter,
        luftdruck
    )

    kategorien["Wetter"] = {
        "punkte": punkte,
        "max": 35,
        "gruende": gruende
    }

    # ----------------------------------------------------------
    # Wasserqualität
    # ----------------------------------------------------------

    punkte, gruende = bewerte_wasser(wasser)

    kategorien["Wasserqualität"] = {
        "punkte": punkte,
        "max": 45,
        "gruende": gruende
    }

    # ----------------------------------------------------------
    # Hydrologie
    # ----------------------------------------------------------

    punkte, gruende = bewerte_hydrologie(
        pegel,
        durchfluss
    )

    kategorien["Hydrologie"] = {
        "punkte": punkte,
        "max": 10,
        "gruende": gruende
    }

    # ----------------------------------------------------------
    # Tageszeit
    # ----------------------------------------------------------

    punkte, gruende = bewerte_tageszeit(tageszeit)

    kategorien["Tageszeit"] = {
        "punkte": punkte,
        "max": 10,
        "gruende": gruende
    }

    # ----------------------------------------------------------
    # Mond
    # ----------------------------------------------------------

    punkte, gruende = bewerte_mond(mond)

    kategorien["Mond"] = {
        "punkte": punkte,
        "max": 10,
        "gruende": gruende
    }

    # ----------------------------------------------------------
    # Gesamt
    # ----------------------------------------------------------

    gesamt = 0
    maximal = 0

    for daten in kategorien.values():
        gesamt += daten["punkte"]
        maximal += daten["max"]

    beissindex = round((gesamt / maximal) * 100)

    return beissindex, kategorien