from fastapi import FastAPI
from dto import VehicleForm
from service.goblin import ScrapingEngine

api = FastAPI()


@api.get("/status")
def status():
    return {"status": 200}


@api.post("/vehicle")
def get_vehicle(form: VehicleForm):
    output = ScrapingEngine(form).execute()

    return output
