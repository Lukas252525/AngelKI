from fastapi import FastAPI

from main import angelki


app = FastAPI(
    title="AngelKI API",
    description="KI Angelanalyse",
    version="1.0"
)


@app.get("/angelki")
def analyse():

    try:
        daten = angelki()
        return daten

    except Exception as e:
        return {
            "fehler": str(e)
        }