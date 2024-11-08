import json
import time

from pprint import pprint

from utils import dict_to_dataclass
from dto import VehicleForm
from vehicle_schema import VehicleRequestOutput
from web_driver import WebDriver

URI_RESPONSE_WITH_DATA = "https://histovec.interieur.gouv.fr/public/v1/report_by_data"


class ScrapingEngine:
    def __init__(self, content: VehicleForm) -> None:
        self.content = content
        self.driver = WebDriver()
        self.driver.run("https://histovec.interieur.gouv.fr/histovec/proprietaire")

    def execute(self):
        if self.content.type == "pro":
            self._professional_process()
        else:
            self._default_process()

        self.driver.find_by_id("bouton-recherche").click()
        time.sleep(5)

        vehicle_str = self._get_response_data()
        vehicle_data = json.loads(vehicle_str)

        vehicle_data = self._clean_vehicle_data(vehicle_data)

        return {"data": vehicle_data}

    def _clean_vehicle_data(self, vehicle_res: VehicleRequestOutput):
        vehicle_copy: VehicleRequestOutput = dict_to_dataclass(
            VehicleRequestOutput, vehicle_res
        )

        if self.content.vin:
            vehicle_copy.vehicule.caracteristiques.vin = self.content.vin
        vehicle_copy.vehicule.infos.plaqueImmatriculation = self.content.immat

        # Anonymize the owner
        vehicle_copy.incomingQuery = None
        vehicle_copy.plaqImmatHash = None

        return vehicle_copy

    def _professional_process(self):
        return {"data": 501}

    def _default_process(self):
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

    def _get_response_data(self) -> str:
        return list(
            filter(
                lambda x: x.response and x.url.startswith(URI_RESPONSE_WITH_DATA),
                self.driver.driver.requests,
            )
        )[0].response.body.decode()
