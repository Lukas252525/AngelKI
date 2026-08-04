from wetter import wetter_laden
from wasser import wasser_laden

from wetter_trends import (
    erstelle_luftdruck_trend,
    erstelle_temperatur_trend,
    erstelle_bewoelkung_trend,
    erstelle_niederschlag_trend
)

from angelprognose import berechne_prognose_aktivitaet



wetter = wetter_laden()


wetter["luftdruck_trend"] = erstelle_luftdruck_trend(wetter)
wetter["temperatur_trend"] = erstelle_temperatur_trend(wetter)
wetter["bewoelkung_trend"] = erstelle_bewoelkung_trend(wetter)
wetter["niederschlag_trend"] = erstelle_niederschlag_trend(wetter)



wasser = wasser_laden()



print("===================")
print("ANGELPROGNOSE TEST")
print("===================")



for fisch in [
    "Wels",
    "Zander",
    "Barsch",
    "Hecht"
]:

    ergebnis = berechne_prognose_aktivitaet(
        fisch,
        wetter,
        wasser
    )


    print()

    print(
        ergebnis
    )