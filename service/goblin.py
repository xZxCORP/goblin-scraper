import json
import requests
import time

from pprint import pprint
from seleniumwire import webdriver
from seleniumwire.utils import decode

from dto import VehicleForm
from web_driver import WEB_DRIVER

URI_RESPONSE_WITH_DATA = "https://histovec.interieur.gouv.fr/public/v1/report_by_data"


class ScrapingEngine:
    def __init__(self, content: VehicleForm) -> None:
        self.content = content
        self.driver = WEB_DRIVER()
        self.driver.run("https://histovec.interieur.gouv.fr/histovec/proprietaire")

    def execute(self):
        if self.content.type == "pro":
            self.professional_process()
        else:
            self.default_process()

        self.driver.find_by_id("bouton-recherche").click()
        time.sleep(5)

        data = self.get_response_data()
        return {"data": data}

    def professional_process(self):
        return {"data": 501}

    def default_process(self):
        time.sleep(3)

        tag = self.driver.find_by_tag("label", array=False)
        self.driver.move_to_element_click(tag)

        time.sleep(5)

        self.driver.find_by_id("form-siv-particulier-nom-naissance").send_keys(
            self.content.nom
        )
        self.driver.find_by_id("form-siv-particulier-prenom").send_keys(
            self.content.prenom
        )
        self.driver.find_by_id("form-siv-particulier-numero-immatriculation").send_keys(
            self.content.immat
        )
        self.driver.find_by_id("form-siv-particulier-numero-formule").send_keys(
            self.content.numeroFormule
        )
        return

    def get_response_data(self) -> str:
        return list(
            filter(
                lambda x: x.response and x.url.startswith(URI_RESPONSE_WITH_DATA),
                self.driver.driver.requests,
            )
        )[0].response.body.decode()
