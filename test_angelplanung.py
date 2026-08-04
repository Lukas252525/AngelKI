from wetter import wetter_laden
from wasser import wasser_laden

from angelplanung import erstelle_angelplanung



wetter = wetter_laden()

wasser = wasser_laden()



print("===================")
print("ANGELPLAN HEUTE")
print("===================")



plan = erstelle_angelplanung(
    wetter,
    wasser
)



for eintrag in plan:


    print()

    print(
        eintrag["fisch"]
    )

    print(
        "Aktivität:",
        eintrag["aktivitaet"]
    )

    print(
        "Zeit:",
        eintrag["beste_zeit"]
    )

    print(
        eintrag["beschreibung"]
    )

    print(
        eintrag["gruende"]
    )