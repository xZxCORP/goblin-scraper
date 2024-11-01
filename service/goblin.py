import json
from pprint import pprint
import time
import requests
from seleniumwire import webdriver
from seleniumwire.utils import decode
from web_driver import WEB_DRIVER

DEFAULT_CONTENT = {
    "nom": "Garo",
    "prenom": "Nino",
    "numeroFormule": "2023AT14081",
    "immat": "DM-190-ZH",
}


class ScrapingEngine:
    def __init__(self, content=None) -> None:
        self.content = content if content else DEFAULT_CONTENT
        self.driver = WEB_DRIVER()
        self.driver.run("https://histovec.interieur.gouv.fr/histovec/proprietaire")

    def __call__(self) -> str:
        time.sleep(3)

        tag = self.driver.find_by_tag("label", array=False)
        self.driver.move_to_element_click(tag)

        time.sleep(5)

        self.driver.find_by_id("form-siv-particulier-nom-naissance").send_keys(
            self.content["nom"]
        )
        self.driver.find_by_id("form-siv-particulier-prenom").send_keys(
            self.content["prenom"]
        )
        self.driver.find_by_id("form-siv-particulier-numero-immatriculation").send_keys(
            self.content["immat"]
        )
        self.driver.find_by_id("form-siv-particulier-numero-formule").send_keys(
            self.content["numeroFormule"]
        )

        self.driver.find_by_id("bouton-recherche").click()

        time.sleep(5)

        data = self.get_response_data()
        return {"data": data}

    def get_response_data(self) -> str:
        return list(
            filter(
                lambda x: x.response
                and x.url.startswith(
                    "https://histovec.interieur.gouv.fr/public/v1/report_by_data"
                ),
                self.driver.driver.requests,
            )
        )[0].response.body.decode()
