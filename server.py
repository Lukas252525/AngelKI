from fastapi import FastAPI

from main import angelki


app = FastAPI(
    title="AngelKI API",
    description="KI Angelanalyse",
    version="1.0"
)


@app.get("/")
def start():

    return {
        "status": "AngelKI läuft"
    }



@app.get("/angelki")
def analyse():

    daten = angelki()

    return daten