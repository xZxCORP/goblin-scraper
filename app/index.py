import traceback

from fastapi import FastAPI, HTTPException
from dto import VehicleForm
from service.goblin import ScrapingEngine

api = FastAPI()


@api.get("/status")
def status():
    return {"status": 200}


@api.post("/vehicle")
def get_vehicle(form: VehicleForm):
    try:
        output = ScrapingEngine(form).execute()

        return output
    except Exception as e:
        traceback.print_exc(e),
        raise HTTPException(
            status_code=500, detail="Something wrong happened when scraping"
        )
