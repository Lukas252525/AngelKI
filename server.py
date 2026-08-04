from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import main
from main import angelki

print("SERVER IMPORT:", main.__file__)


app = FastAPI(
    title="AngelKI API",
    description="KI Angelanalyse",
    version="1.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
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