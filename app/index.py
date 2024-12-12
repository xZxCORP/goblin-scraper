import traceback

from fastapi import FastAPI, HTTPException, Response
from dto import VehicleForm
from service.goblin import ScrapingEngine

api = FastAPI()


@api.get("/status")
def status():
    return {"status": 200}


@api.post("/vehicle")
def get_vehicle(form: VehicleForm, response: Response):
    try:
        output = ScrapingEngine(form).execute()
        if output["data"] is not None:
            response.status_code = 200
        else:
            response.status_code = 404
        return output
    except Exception as e:
        traceback.print_exc(e),
        raise HTTPException(
            status_code=500, detail="Something wrong happened when scraping"
        )
