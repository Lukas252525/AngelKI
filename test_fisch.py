from empfehlung import erstelle_empfehlung
from wetter import wetter_laden
from wasser import wasser_laden
from tageszeit import tageszeit_laden
from mond import mond_laden
from durchfluss import durchfluss_laden


wetter = wetter_laden()

wasser = wasser_laden()

mond = mond_laden()

tageszeit = tageszeit_laden(
    mond
)

durchfluss = durchfluss_laden()



empfehlung = erstelle_empfehlung(
    wetter,
    wasser,
    tageszeit,
    durchfluss
)



print("===================")
print("FISCH TEST")
print("===================")

print(
    empfehlung["fisch"]
)

print(
    empfehlung
)