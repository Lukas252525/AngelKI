import requests


def pegel_laden():

    url = "https://www.geoportal.rlp.de/spatial-objects/281/collections/gk:waterlevels/items?f=json&limit=1000"

    daten = requests.get(url).json()

    for eintrag in daten["features"]:

        eig = eintrag["properties"]

        if eig["station"] == "ZELTINGEN UP":

            return {

                "station": eig["station"],
                "pegel": eig["value"],
                "einheit": eig["unit"],
                "zeit": eig["date"],
                "status": eig["status"]

            }

    return None


if __name__ == "__main__":

    print(pegel_laden())