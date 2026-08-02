import time


speicher = {}


def holen(name):

    if name in speicher:

        daten, zeit = speicher[name]

        alter = time.time() - zeit

        # 15 Minuten gültig
        if alter < 900:
            return daten


    return None



def speichern(name, daten):

    speicher[name] = (
        daten,
        time.time()
    )