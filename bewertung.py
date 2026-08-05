from datetime import datetime
from wissen import *

# ----------------------------------------------------------
# Wasserqualität
# ----------------------------------------------------------

def bewerte_wassertemperatur(temperatur):

    if WASSERTEMPERATUR_OPTIMAL[0] <= temperatur <= WASSERTEMPERATUR_OPTIMAL[1]:
        return 13, "Optimale Wassertemperatur"

    elif WASSERTEMPERATUR_GUT[0] <= temperatur < WASSERTEMPERATUR_GUT[1]:
        return 10, "Gute Wassertemperatur"

    elif WASSERTEMPERATUR_NOCH_GUT[0] < temperatur <= WASSERTEMPERATUR_NOCH_GUT[1]:
        return 18, "Noch gute Wassertemperatur"

    elif WASSERTEMPERATUR_WARM[0] < temperatur <= WASSERTEMPERATUR_WARM[1]:
        return 3, "Wasser recht warm"

    return 0, "Ungünstige Wassertemperatur"


def bewerte_sauerstoff(sauerstoff):

    if sauerstoff >= SAUERSTOFF_SEHR_GUT:
        return 12, "Sehr hoher Sauerstoff"

    elif sauerstoff >= SAUERSTOFF_GUT:
        return 8, "Guter Sauerstoff"

    elif sauerstoff >= SAUERSTOFF_AUSREICHEND:
        return 4, "Ausreichender Sauerstoff"

    return 0, "Wenig Sauerstoff"


def bewerte_truebung(truebung):

    if TRUEBUNG_OPTIMAL[0] <= truebung <= TRUEBUNG_OPTIMAL[1]:
        return 8, "Gute Trübung"

    elif TRUEBUNG_ERHOEHT[0] < truebung <= TRUEBUNG_ERHOEHT[1]:
        return 5, "Erhöhte Trübung"

    return 0, "Ungünstige Trübung"


def bewerte_blaualgen(blaualgen):

    if blaualgen < BLAUALGEN_GERING:
        return 4, "Kaum Blaualgen"

    elif blaualgen < BLAUALGEN_ERHOEHT:
        return 2, "Leichte Blaualgenbelastung"

    return 0, "Viele Blaualgen"


# ----------------------------------------------------------
# Hydrologie
# ----------------------------------------------------------

def bewerte_durchfluss(durchfluss):

    if DURCHFLUSS_OPTIMAL[0] <= durchfluss <= DURCHFLUSS_OPTIMAL[1]:
        return 4, "Optimaler Durchfluss"

    elif DURCHFLUSS_NIEDRIG[0] <= durchfluss < DURCHFLUSS_NIEDRIG[1]:
        return 3, "Niedriger Durchfluss"

    elif DURCHFLUSS_STARK_NIEDRIG[0] <= durchfluss < DURCHFLUSS_STARK_NIEDRIG[1]:
        return 1, "Starkes Niedrigwasser"

    elif DURCHFLUSS_HOCH[0] < durchfluss <= DURCHFLUSS_HOCH[1]:
        return 2, "Erhöhter Durchfluss"

    elif durchfluss > DURCHFLUSS_HOCH[1]:
        return 0, "Sehr hoher Durchfluss"

    return 0, "Extremes Niedrigwasser"


def bewerte_pegel(pegel):

    if pegel <= PEGEL_NORMAL_MAX:
        return 4, "Normaler Staupegel"

    elif pegel <= PEGEL_ERHOEHT_MAX:
        return 2, "Erhöhter Pegel"

    return 0, "Hochwasser"


# ----------------------------------------------------------
# Tageszeit
# ----------------------------------------------------------

def bewerte_tageszeit(tageszeit):

    phase = tageszeit["phase"]

    if "Morgenbeißzeit" in phase:
        return 9, ["Morgenbeißzeit"]

    elif "Abendbeißzeit" in phase:
        return 9, ["Abendbeißzeit"]

    elif "Nacht" in phase:
        return 7, ["Nacht"]

    return 3, ["Tagesphase"]


# ----------------------------------------------------------
# Wetter
# ----------------------------------------------------------

def bewerte_luftdruck(luftdruck):

    if LUFTDRUCK_OPTIMAL[0] <= luftdruck <= LUFTDRUCK_OPTIMAL[1]:
        return 4, "Stabiler Luftdruck"

    return 0, "Ungünstiger Luftdruck"


def bewerte_luftdrucktrend(luftdruck):

    if luftdruck["differenz"] >= LUFTDRUCK_STEIGEND:
        return 8, "Steigender Luftdrucktrend"

    elif luftdruck["differenz"] <= LUFTDRUCK_FALLEND:
        return 2, "Fallender Luftdrucktrend"

    return 6, "Stabiler Luftdrucktrend"


def bewerte_wind(wind):

    if WIND_OPTIMAL[0] <= wind <= WIND_OPTIMAL[1]:
        return 8, "Optimaler Wind"

    return 0, "Ungünstiger Wind"


def bewerte_bewoelkung(bewoelkung):

    if BEWOELKUNG_OPTIMAL[0] <= bewoelkung <= BEWOELKUNG_OPTIMAL[1]:
        return 8, "Gute Bewölkung"

    elif BEWOELKUNG_GUT[0] <= bewoelkung < BEWOELKUNG_GUT[1]:
        return 5, "Leichte Bewölkung"

    return 2, "Klarer Himmel"


# ----------------------------------------------------------
# Jahreszeit
# ----------------------------------------------------------

def bewerte_jahreszeit(wetter):

    monat = datetime.now().month

    if monat in [3, 4, 5]:
        return 15, ["Frühling"]

    elif monat in [6, 7, 8]:
        return 15, ["Sommer"]

    elif monat in [9, 10, 11]:
        return 15, ["Herbst"]

    return 15, ["Winter"]


# ----------------------------------------------------------
# Wasserqualität
# ----------------------------------------------------------

def bewerte_wasser(wasser):

    punkte = 0
    gruende = []

    for funktion, wert in [
        (bewerte_wassertemperatur, wasser["wassertemperatur"]),
        (bewerte_sauerstoff, wasser["sauerstoff"]),
        (bewerte_truebung, wasser["truebung"]),
        (bewerte_blaualgen, wasser["blaualgen"])
    ]:

        p, g = funktion(wert)
        punkte += p
        gruende.append(g)

    return punkte, gruende


# ----------------------------------------------------------
# Hydrologie
# ----------------------------------------------------------

def bewerte_hydrologie(pegel, durchfluss):

    punkte = 0
    gruende = []

    for funktion, wert in [
        (bewerte_pegel, pegel["pegel"]),
        (bewerte_durchfluss, durchfluss["durchfluss"])
    ]:

        p, g = funktion(wert)
        punkte += p
        gruende.append(g)

    return punkte, gruende


# ----------------------------------------------------------
# Wetter
# ----------------------------------------------------------

def bewerte_wetter(wetter, luftdruck):

    punkte = 0
    gruende = []

    for funktion, wert in [
        (bewerte_luftdruck, wetter["pressure_msl"]),
        (bewerte_luftdrucktrend, luftdruck),
        (bewerte_wind, wetter["wind_speed_10m"]),
        (bewerte_bewoelkung, wetter["cloud_cover"])
    ]:

        p, g = funktion(wert)
        punkte += p
        gruende.append(g)

    return punkte, gruende


# ----------------------------------------------------------
# Mond
# ----------------------------------------------------------

def bewerte_mond(mond):

    phase = mond["wert"]

    if phase < 0.15 or phase > 0.85:
        return 8, ["Günstige Mondphase"]

    elif 0.40 <= phase <= 0.60:
        return 6, ["Vollmondnähe"]

    return 4, ["Neutrale Mondphase"]