def wetterprognose_erstellen(wetter):

    prognose = []


    # ----------------------------------
    # Temperatur
    # ----------------------------------

    temp = wetter["temperatur_trend"]

    jetzt = temp["jetzt"]
    spaeter = temp["wert_24h"]


    prognose.append("🌡 Temperaturtrend (24h)")

    prognose.append(
        f"{wetter['uhrzeit']}   {jetzt} °C"
    )

    prognose.append(
        f"{temp['zeit_24h']}   {spaeter} °C"
    )


    unterschied = round(spaeter - jetzt, 1)


    if unterschied <= -3:

        prognose.append(
            f"✓ starke Abkühlung ({unterschied} °C)"
        )

    elif unterschied < 0:

        prognose.append(
            f"✓ leichte Abkühlung ({unterschied} °C)"
        )

    elif unterschied >= 3:

        prognose.append(
            f"⚠ starke Erwärmung (+{unterschied} °C)"
        )

    else:

        prognose.append(
            "→ Temperatur stabil"
        )



    prognose.append("")



    # ----------------------------------
    # Bewölkung
    # ----------------------------------

    wolken = wetter["bewoelkung_trend"]


    prognose.append("☁ Bewölkung (6h)")


    prognose.append(
        f"{wetter['uhrzeit']}   {wolken['jetzt']} %"
    )


    prognose.append(
        f"{wolken['zeit_6h']}   {wolken['wert_6h']} %"
    )


    if wolken["wert_6h"] > wolken["jetzt"] + 20:

        prognose.append(
            "✓ zunehmende Bewölkung"
        )

    elif wolken["wert_6h"] < wolken["jetzt"] - 20:

        prognose.append(
            "☀ Himmel klart auf"
        )

    else:

        prognose.append(
            "→ Bewölkung ähnlich"
        )



    prognose.append("")



    # ----------------------------------
    # Luftdruck
    # ----------------------------------

    druck = wetter["luftdruck_trend"]


    prognose.append("📉 Luftdrucktrend (24h)")


    prognose.append(
        f"Jetzt          {druck['jetzt']} hPa"
    )


    prognose.append(
        f"{druck['zeit_24h']}   {druck['wert_24h']} hPa"
    )


    differenz = round(
        druck["wert_24h"] - druck["jetzt"],
        1
    )


    if abs(differenz) < 2:

        prognose.append(
            "✓ Luftdruck stabil"
        )

    elif differenz > 0:

        prognose.append(
            f"↑ leichter Anstieg (+{differenz} hPa)"
        )

    else:

        prognose.append(
            f"↓ leichter Abfall ({differenz} hPa)"
        )



    prognose.append("")



    # ----------------------------------
    # Regen
    # ----------------------------------

    regen = wetter["niederschlag_trend"]


    prognose.append("🌧 Niederschlag (6h)")


    prognose.append(
        f"Erwartet: {regen['menge']} mm"
    )


    if regen["menge"] == 0:

        prognose.append(
            "✓ trocken"
        )

    elif regen["menge"] < 2:

        prognose.append(
            "→ leichter Regen möglich"
        )

    else:

        prognose.append(
            "⚠ Regen erwartet"
        )


    return prognose