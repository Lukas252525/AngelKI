import requests


def durchfluss_laden():

    url = (
        "https://www.pegelonline.wsv.de/webservices/rest-api/v2/"
        "stations/768df4e9-ed5a-4141-901b-e25ac404d559/"
        "Q/currentmeasurement.json"
    )

    daten = requests.get(url).json()

    zeit = daten["timestamp"]

    datum = zeit[:10]
    uhrzeit = zeit[11:16]

    jahr, monat, tag = datum.split("-")

    return {

        "datum": f"{tag}.{monat}.{jahr}",
        "uhrzeit": uhrzeit,
        "durchfluss": daten["value"]

    }


if __name__ == "__main__":

    print(durchfluss_laden())