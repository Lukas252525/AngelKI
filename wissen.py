# ----------------------------
# Wassertemperatur
# ----------------------------

WASSERTEMPERATUR_OPTIMAL = (18, 24)
WASSERTEMPERATUR_GUT = (15, 18)
WASSERTEMPERATUR_NOCH_GUT = (24, 26)
WASSERTEMPERATUR_WARM = (26, 28)

# ----------------------------
# Sauerstoff
# ----------------------------

SAUERSTOFF_SEHR_GUT = 10
SAUERSTOFF_GUT = 8
SAUERSTOFF_AUSREICHEND = 6

# ----------------------------
# Trübung
# ----------------------------

TRUEBUNG_OPTIMAL = (5, 20)
TRUEBUNG_ERHOEHT = (20, 40)

# ----------------------------
# Blaualgen
# ----------------------------

BLAUALGEN_GERING = 20
BLAUALGEN_ERHOEHT = 50

# ----------------------------
# Wetter
# ----------------------------

LUFTDRUCK_OPTIMAL = (1010, 1022)

WIND_OPTIMAL = (5, 18)

BEWOELKUNG_OPTIMAL = (30, 100)
BEWOELKUNG_GUT = (10, 30)

# ----------------------------
# Luftdrucktrend
# ----------------------------

LUFTDRUCK_STEIGEND = 2.0
LUFTDRUCK_FALLEND = -2.0

# ----------------------------
# Durchfluss Mosel
# ----------------------------

DURCHFLUSS_OPTIMAL = (80, 400)
DURCHFLUSS_NIEDRIG = (58, 80)
DURCHFLUSS_STARK_NIEDRIG = (40, 58)
DURCHFLUSS_HOCH = (400, 700)

# ----------------------------
# Pegel Mosel (gestaut)
# ----------------------------

PEGEL_NORMAL_MAX = 330
PEGEL_ERHOEHT_MAX = 420

# ----------------------------
# Funktionen
# ----------------------------

def blaualgen_status(wert):

    if wert < BLAUALGEN_GERING:
        return "🟢", "Unkritisch"

    elif wert < BLAUALGEN_ERHOEHT:
        return "🟡", "Erhöht"

    return "🔴", "Kritisch"