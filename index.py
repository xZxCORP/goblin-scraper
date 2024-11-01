from typing import Union
from fastapi import FastAPI
from service.goblin import ScrapingEngine

api = FastAPI()


@api.get("/status")
def status():
    return {"status": 200}


@api.get("/vehicle")
def get_vehicle():
    output = ScrapingEngine()()

    return output
