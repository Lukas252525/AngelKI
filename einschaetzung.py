def erstelle_einschaetzung(kategorien, tageszeit):

    texte = []

    if kategorien["Wasserqualität"]["punkte"] >= 35:
        texte.append("✓ Die Wasserqualität ist aktuell hervorragend.")

    elif kategorien["Wasserqualität"]["punkte"] >= 25:
        texte.append("✓ Die Wasserqualität ist gut.")

    else:
        texte.append("⚠️ Die Wasserqualität ist eher ungünstig.")

    if kategorien["Hydrologie"]["punkte"] <= 3:
        texte.append("⚠️ Sehr geringer Durchfluss kann die Fischaktivität bremsen.")

    elif kategorien["Hydrologie"]["punkte"] >= 8:
        texte.append("✓ Gute hydrologische Bedingungen.")

    if tageszeit["phase"] == "☀️ Tagesphase":
        texte.append(
            f"🌇 Die nächste starke Beißphase beginnt in {tageszeit['restzeit']}."
        )

    elif tageszeit["phase"] == "🌅 Morgenbeißzeit":
        texte.append("🎣 Aktuell läuft die Morgenbeißzeit.")

    elif tageszeit["phase"] == "🌇 Abendbeißzeit":
        texte.append("🎣 Aktuell läuft die Abendbeißzeit.")

    elif tageszeit["phase"] == "🌙 Nacht":
        texte.append("🌙 Nachtaktive Fischarten werden jetzt interessanter.")

    return texte