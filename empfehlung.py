from barsch import berechne as barsch_berechne
from zander import berechne as zander_berechne
from hecht import berechne as hecht_berechne
from wels import berechne as wels_berechne


def erstelle_empfehlung(
    wetter,
    wasser,
    tageszeit,
    durchfluss
):

    barsch = barsch_berechne(
        wetter,
        wasser,
        tageszeit,
        durchfluss
    )

    zander = zander_berechne(
        wetter,
        wasser,
        tageszeit,
        durchfluss
    )

    hecht = hecht_berechne(
        wetter,
        wasser,
        tageszeit,
        durchfluss
    )

    wels = wels_berechne(
        wetter,
        wasser,
        tageszeit,
        durchfluss
    )

    ranking = [
        barsch,
        zander,
        hecht,
        wels
    ]

    ranking.sort(
        key=lambda x: x["punkte"],
        reverse=True
    )

    bester = ranking[0]

    return {

    "fisch": bester["fisch"],

    "chance": bester["punkte"],

    "spot": bester["spot"],

    "methode": bester["methode"],

    "tiefe": bester["tiefe"],

    "farbe": bester.get("farbe"),

    "kontrast": bester.get("kontrast"),

    "natuerlichkeit": bester.get("natuerlichkeit"),

    "glitzer": bester.get("glitzer"),

    "gruende": bester["gruende"],

    "methoden_ranking": bester["methoden_ranking"],

    "ranking": ranking

}