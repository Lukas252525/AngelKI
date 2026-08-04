from wetter import wetter_laden
from wasser import wasser_laden
from empfehlung import erstelle_empfehlung

from wetter_trends import (
    erstelle_luftdruck_trend,
    erstelle_temperatur_trend,
    erstelle_bewoelkung_trend,
    erstelle_niederschlag_trend
)

from angelzeit import berechne_angelzeit



print("===================")
print("ANGELZEIT TEST")
print("===================")



wetter = wetter_laden()



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



wasser = wasser_laden()



empfehlung = {

    "fisch":
    "Wels"

}



ergebnis = berechne_angelzeit(
    wetter,
    wasser,
    empfehlung
)



print(ergebnis)