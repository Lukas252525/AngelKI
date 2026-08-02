from datetime import datetime, timedelta


def format_dauer(dauer):

    minuten = int(dauer.total_seconds() / 60)

    stunden = minuten // 60
    minuten = minuten % 60

    return f"{stunden} h {minuten} min"


def tageszeit_laden(mond):

    jetzt = datetime.now()

    sonnenaufgang = datetime.fromisoformat(mond["sonnenaufgang"])
    sonnenuntergang = datetime.fromisoformat(mond["sonnenuntergang"])

    morgen_start = sonnenaufgang - timedelta(hours=1)
    morgen_ende = sonnenaufgang + timedelta(hours=2)

    abend_start = sonnenuntergang - timedelta(hours=3)
    abend_ende = sonnenuntergang + timedelta(hours=1)

    if morgen_start <= jetzt < morgen_ende:

        phase = "🌅 Morgenbeißzeit"
        naechste = "☀️ Tagesphase"
        rest = morgen_ende - jetzt

    elif morgen_ende <= jetzt < abend_start:

        phase = "☀️ Tagesphase"
        naechste = "🌇 Abendbeißzeit"
        rest = abend_start - jetzt

    elif abend_start <= jetzt < abend_ende:

        phase = "🌇 Abendbeißzeit"
        naechste = "🌙 Nacht"
        rest = abend_ende - jetzt

    else:

        phase = "🌙 Nacht"
        naechste = "🌅 Morgenbeißzeit"

        if jetzt > morgen_start:
            rest = (morgen_start + timedelta(days=1)) - jetzt
        else:
            rest = morgen_start - jetzt

    if jetzt >= sonnenaufgang:
        seit = format_dauer(jetzt - sonnenaufgang)
    else:
        seit = "-"

    if jetzt <= sonnenuntergang:
        bis = format_dauer(sonnenuntergang - jetzt)
    else:
        bis = "-"

    return {

        "jetzt": jetzt.strftime("%H:%M"),

        "phase": phase,

        "sonnenaufgang": sonnenaufgang.strftime("%H:%M"),

        "sonnenuntergang": sonnenuntergang.strftime("%H:%M"),

        "seit_sonnenaufgang": seit,

        "bis_sonnenuntergang": bis,

        "naechste_phase": naechste,

        "restzeit": format_dauer(rest)

    }


if __name__ == "__main__":

    from mond import mond_laden

    print(tageszeit_laden(mond_laden()))