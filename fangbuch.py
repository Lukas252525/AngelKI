import json
import os

DATEI = "daten/fangbuch.json"


def lade_faenge():

    if not os.path.exists(DATEI):
        return []

    with open(DATEI, "r", encoding="utf-8") as f:
        return json.load(f)


def speichere_fang(fang):

    faenge = lade_faenge()

    faenge.append(fang)

    with open(DATEI, "w", encoding="utf-8") as f:
        json.dump(faenge, f, indent=4, ensure_ascii=False)