import json
from dto import VehicleForm
from vehicle_schema import VehicleRequestOutput
from web_driver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

URI_RESPONSE_WITH_DATA = "https://histovec.interieur.gouv.fr/public/v1/report_by_data"


class ScrapingEngine:
    def __init__(self, content: VehicleForm) -> None:
        self.content = content
        self.driver = WebDriver()

    def execute(self):
        self.driver.run("https://histovec.interieur.gouv.fr/histovec/proprietaire")
        if self.content.type == "pro":
            self._professional_process()
        else:
            self._default_process()

        WebDriverWait(self.driver.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "bouton-recherche"))
        )
        self.driver.find_by_id("bouton-recherche").click()

        WebDriverWait(self.driver.driver, 10).until(
            lambda driver: any(
                x.response and x.url.startswith(URI_RESPONSE_WITH_DATA)
                for x in driver.requests
            )
        )

        vehicle_str = self._get_response_data()
        vehicle_data: VehicleRequestOutput = json.loads(vehicle_str)
        if vehicle_data.get("vehicule") is None:
            return {"data": None}
        vehicle_data = self._clean_vehicle_data(vehicle_data)

        return {"data": vehicle_data}

    def _clean_vehicle_data(self, vehicle_res: VehicleRequestOutput):
        vehicle_copy: VehicleRequestOutput = vehicle_res.copy()

        if self.content.vin:
            vehicle_copy["vehicule"]["caracteristiques"]["vin"] = self.content.vin
        vehicle_copy["vehicule"]["infos"]["plaqueImmatriculation"] = self.content.immat

        # Anonymize the owner
        vehicle_copy["incomingQuery"] = None
        vehicle_copy["plaqImmatHash"] = None

        return vehicle_copy

    def _professional_process(self):
        return {"data": 501}

    def _default_process(self):
        WebDriverWait(self.driver.driver, 10).until(
            EC.visibility_of_element_located((By.TAG_NAME, "label"))
        )
        tag = self.driver.find_by_tag("label", array=False)
        self.driver.move_to_element_click(tag)

        WebDriverWait(self.driver.driver, 10).until(
            EC.visibility_of_element_located(
                (By.ID, "form-siv-particulier-nom-naissance")
            )
        )
        self.driver.find_by_id("form-siv-particulier-nom-naissance").send_keys(
            self.content.nom
        )

        WebDriverWait(self.driver.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "form-siv-particulier-prenom"))
        )
        self.driver.find_by_id("form-siv-particulier-prenom").send_keys(
            self.content.prenom
        )

        WebDriverWait(self.driver.driver, 10).until(
            EC.visibility_of_element_located(
                (By.ID, "form-siv-particulier-numero-immatriculation")
            )
        )
        self.driver.find_by_id("form-siv-particulier-numero-immatriculation").send_keys(
            self.content.immat
        )

        WebDriverWait(self.driver.driver, 10).until(
            EC.visibility_of_element_located(
                (By.ID, "form-siv-particulier-numero-formule")
            )
        )
        self.driver.find_by_id("form-siv-particulier-numero-formule").send_keys(
            self.content.numeroFormule
        )

    def _get_response_data(self) -> str:
        return list(
            filter(
                lambda x: x.response and x.url.startswith(URI_RESPONSE_WITH_DATA),
                self.driver.driver.requests,
            )
        )[0].response.body.decode()
