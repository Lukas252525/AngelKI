from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

import main
from main import angelki


print("SERVER IMPORT:", main.__file__)



app = FastAPI(
    title="AngelKI API",
    description="KI Angelanalyse",
    version="1.0"
)



# ----------------------------------
# Frontend bereitstellen
# ----------------------------------

app.mount(
    "/frontend",
    StaticFiles(directory="frontend"),
    name="frontend"
)



# ----------------------------------
# CORS
# ----------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)



# ----------------------------------
# AngelKI API
# ----------------------------------

@app.get("/angelki")
def analyse():

    try:

        daten = angelki()

        return daten


    except Exception as e:

        return {
            "fehler": str(e)
        }



# ----------------------------------
# Startseite
# ----------------------------------

@app.get("/")
def startseite():

    return FileResponse(
        "frontend/index.html"
    )