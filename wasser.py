from playwright.sync_api import sync_playwright
import re

URL = "https://geodaten-wasser.rlp-umwelt.de/gus/2691510700/messwerte"


def finde(text, name):

    m = re.search(rf"{name}\s+([\d,]+)", text)

    if not m:
        return None

    return float(m.group(1).replace(",", "."))


def wasser_laden():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)

        page = browser.new_page()

        page.goto(URL)

        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(2000)

        text = page.locator("body").inner_text()

        browser.close()

    # Datum auslesen
    datum = ""

    m = re.search(r"Datum\s+(\d{2}\.\d{2}\.\d{4})", text)

    if m:
        datum = m.group(1)

    # Uhrzeit auslesen
    uhrzeit = ""

    m = re.search(r"Uhrzeit.*?(\d{2}:\d{2})", text, re.DOTALL)

    if m:
        uhrzeit = m.group(1)

    return {

        "datum": datum,
        "uhrzeit": uhrzeit,

        "wassertemperatur": finde(text, "Wassertemperatur"),
        "sauerstoff": finde(text, "Sauerstoff"),
        "ph": finde(text, "pH-Wert"),
        "leitfaehigkeit": finde(text, "Elektrische Leitfähigkeit bei 25°C"),
        "truebung": finde(text, "Trübung"),
        "nitrat": finde(text, "Nitrat-Stickstoff"),
        "gesamtchlorophyll": finde(text, "Gesamtchlorophyll a"),
        "blaualgen": finde(text, "Blaualgenchlorophyll a"),
    }