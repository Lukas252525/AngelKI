from wetter import wetter_laden
from wasser import wasser_laden
from mond import mond_laden
from tageszeit import tageszeit_laden
from luftdruck import luftdrucktrend_laden
from pegel import pegel_laden
from durchfluss import durchfluss_laden

from beissindex import berechne_beissindex
from einschaetzung import erstelle_einschaetzung
from empfehlung import erstelle_empfehlung

from wissen import blaualgen_status
from wetterprognose import wetterprognose_erstellen
from wetterbewertung import bewerte_wetterprognose

from config import GEWAESSER



def formatiere_datum(datum):

    jahr, monat, tag = datum.split("-")

    return f"{tag}.{monat}.{jahr}"



def formatiere_iso(zeit):

    datum = zeit[:10]
    uhr = zeit[11:16]

    jahr, monat, tag = datum.split("-")

    return f"{tag}.{monat}.{jahr} {uhr}"



def hauptprogramm():

    wetter = wetter_laden()
    wasser = wasser_laden()
    mond = mond_laden()

    tageszeit = tageszeit_laden(mond)

    luftdruck = luftdrucktrend_laden()

    pegel = pegel_laden()

    durchfluss = durchfluss_laden()


    wetterprognose = wetterprognose_erstellen(wetter)

    wetterbewertung = bewerte_wetterprognose(wetter)



    beissindex, kategorien = berechne_beissindex(
        wetter,
        wasser,
        mond,
        tageszeit,
        luftdruck,
        durchfluss,
        pegel
    )



    einschaetzung = erstelle_einschaetzung(
        kategorien,
        tageszeit
    )



    empfehlung = erstelle_empfehlung(
        wetter,
        wasser,
        tageszeit,
        durchfluss
    )



    symbol, status = blaualgen_status(
        wasser["blaualgen"]
    )



    print("=" * 65)

    print("🐟 AngelKI v1.3")

    print("=" * 65)



    print(f"\n📍 Gewässer: {GEWAESSER}")



    # ----------------------------------
    # Wetter
    # ----------------------------------

    print("\n🌤 Wetter")

    print("-" * 65)

    print(
        f"Messung:           "
        f"{formatiere_datum(wetter['datum'])} {wetter['uhrzeit']}"
    )

    print(
        f"Temperatur:        {wetter['temperature_2m']} °C"
    )

    print(
        f"Gefühlt:           {wetter['apparent_temperature']} °C"
    )

    print(
        f"Luftdruck:         {wetter['pressure_msl']} hPa"
    )

    print(
        f"Luftdrucktrend:    "
        f"{luftdruck['trend']} "
        f"({luftdruck['differenz']} hPa / 24h)"
    )

    print(
        f"Bewölkung:         {wetter['cloud_cover']} %"
    )

    print(
        f"Niederschlag:      {wetter['precipitation']} mm"
    )



    # ----------------------------------
    # Wetterprognose
    # ----------------------------------

    print("\n🌦 Wetterprognose")

    print("-" * 65)


    for zeile in wetterprognose:

        print(zeile)



    print()

    print("🎣 Wetterprognose Bewertung")

    print("-" * 65)


    print(
        f"Gesamt: {wetterbewertung['punkte']} "
        f"/ {wetterbewertung['max']}"
    )

    print()


    for grund in wetterbewertung["gruende"]:

        print(f"✓ {grund}")



    # ----------------------------------
    # Wasser
    # ----------------------------------

    print("\n🌊 Wasser")

    print("-" * 65)


    print(
        f"Messung:           "
        f"{wasser['datum']} {wasser['uhrzeit']}"
    )

    print(
        f"Wassertemperatur:  "
        f"{wasser['wassertemperatur']} °C"
    )

    print(
        f"Sauerstoff:        "
        f"{wasser['sauerstoff']} mg/l"
    )

    print(
        f"pH-Wert:           "
        f"{wasser['ph']}"
    )

    print(
        f"Leitfähigkeit:     "
        f"{wasser['leitfaehigkeit']} µS/cm"
    )

    print(
        f"Trübung:           "
        f"{wasser['truebung']} TE"
    )

    print(
        f"Nitrat:            "
        f"{wasser['nitrat']} mg/l"
    )

    print(
        f"Chlorophyll:       "
        f"{wasser['gesamtchlorophyll']} µg/l"
    )

    print(
        f"Blaualgen:         "
        f"{wasser['blaualgen']} µg/l"
    )

    print(
        f"Ampel:             "
        f"{symbol} {status}"
    )



    # ----------------------------------
    # Pegel
    # ----------------------------------

    print("\n📈 Pegel")

    print("-" * 65)

    print(
        f"Station:           {pegel['station']}"
    )

    print(
        f"Messung:           "
        f"{formatiere_iso(pegel['zeit'])}"
    )

    print(
        f"Pegel:             "
        f"{pegel['pegel']} {pegel['einheit']}"
    )


    if pegel["status"] == "up-to-date":

        print("Status:            ✅ Aktuell")

    else:

        print(
            f"Status:            {pegel['status']}"
        )



    # ----------------------------------
    # Durchfluss
    # ----------------------------------

    print("\n🌊 Durchfluss")

    print("-" * 65)

    print(
        f"Messung:           "
        f"{durchfluss['datum']} {durchfluss['uhrzeit']}"
    )

    print(
        f"Durchfluss:        "
        f"{durchfluss['durchfluss']} m³/s"
    )



    # ----------------------------------
    # Mond
    # ----------------------------------

    print("\n🌙 Mond")

    print("-" * 65)

    print(
        f"Phase:             {mond['name']}"
    )

    print(
        f"Sonnenaufgang:     {mond['sonnenaufgang']}"
    )

    print(
        f"Sonnenuntergang:   {mond['sonnenuntergang']}"
    )



    # ----------------------------------
    # Tageszeit
    # ----------------------------------

    print("\n🕒 Tageszeit")

    print("-" * 65)

    print(
        f"Aktuelle Uhrzeit:  {tageszeit['jetzt']}"
    )

    print(
        f"Phase:             {tageszeit['phase']}"
    )

    print()

    print(
        f"Seit Sonnenaufgang: "
        f"{tageszeit['seit_sonnenaufgang']}"
    )

    print(
        f"Bis Sonnenuntergang: "
        f"{tageszeit['bis_sonnenuntergang']}"
    )

    print()

    print(
        f"Nächste Phase:      "
        f"{tageszeit['naechste_phase']}"
    )

    print(
        f"Beginn in:          "
        f"{tageszeit['restzeit']}"
    )



    # ----------------------------------
    # Beißindex
    # ----------------------------------

    print("\n🎣 Beißindex")

    print("-" * 65)


    print(
        f"Gesamt:            "
        f"{beissindex} / 100"
    )

    print()


    for name, daten in kategorien.items():

        print(
            f"{name}: {daten['punkte']} / {daten['max']}"
        )

        for grund in daten["gruende"]:

            print(
                f"   ✓ {grund}"
            )

        print()



    # ----------------------------------
    # Einschätzung
    # ----------------------------------

    print("🧠 Einschätzung")

    print("-" * 65)


    for text in einschaetzung:

        print(text)



    # ----------------------------------
    # Empfehlung
    # ----------------------------------

    print("\n🎯 Empfehlung")

    print("-" * 65)


    print(
        f"Zielfisch:         {empfehlung['fisch']}"
    )

    print(
        f"Chance:            {empfehlung['chance']} / 100"
    )

    print(
        f"Spot:              {empfehlung['spot']}"
    )

    print(
        f"Methode:           {empfehlung['methode']}"
    )

    print(
        f"Tiefe:             {empfehlung['tiefe']}"
    )


    print()


    print("🔧 Methodenbewertung")

    print("-" * 65)


    for name, punkte in empfehlung["methoden_ranking"]:

        print(
            f"{name:<30} {punkte} Punkte"
        )



    print()


    print("🎨 Köderempfehlung")

    print("-" * 65)


    print(
        f"Farbe:             {empfehlung['farbe']}"
    )

    print(
        f"Kontrast:          {empfehlung['kontrast']}"
    )

    print(
        f"Natürlichkeit:     {empfehlung['natuerlichkeit']}"
    )

    print(
        f"Glitzer:           {empfehlung['glitzer']}"
    )



    print()


    print("🏆 Ranking")

    print("-" * 65)


    for platz, daten in enumerate(
        empfehlung["ranking"],
        start=1
    ):

        print(
            f"{platz}. {daten['fisch']:<10} "
            f"{daten['punkte']} / 100"
        )



    print()

    print("=" * 65)





if __name__ == "__main__":

    hauptprogramm()