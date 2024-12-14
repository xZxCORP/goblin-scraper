from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class WebDriver:
    """
    Class Made to regroup all the web related utilities
    """

    def __init__(self):
        """
        Initialization of the variables, and drivers
        """
        self.opts = Options()

        self.opts.add_argument("--no-sandbox")
        self.opts.add_argument("--headless")
        self.opts.add_argument("--disable-dev-shm-usage")
        self.opts.add_argument("--disable-extensions")
        self.opts.add_argument("--disable-gpu")
        self.opts.add_argument("--disable-logging")
        self.opts.add_argument("--log-level=3")

        self.opts.add_argument("--blink-settings=imagesEnabled=false")
        service = ChromeService(executable_path="/usr/bin/chromedriver")
        self.driver = webdriver.Chrome(
            service=service,
            options=self.opts,
            seleniumwire_options={"disable_encoding": True},
        )
        self.action_chains = ActionChains(self.driver)

    def run(self, url: str) -> None:
        """
        Runs the url passed in arg in the Chrome browser
        """
        self.driver.get(url)

    def get_current_url(self) -> str:
        """
        Returns the current url of the page
        """
        return self.driver.current_url

    def get_attribute(self, attribute: str, web_element: WebElement) -> str:
        """
        Returns the attribute passed in parameter of the WebElement also passed in params
        """
        return web_element.get_attribute(attribute)

    def find_by_classname(
        self, name: str, web_element: WebElement = None, array: bool = True
    ):
        """
        Returns the WebElement(s) that are children of the web_element passed in parameters
        If no children is given, then the full page will be searched\n
        If array is True then it will return all the matching elements
        Else only the first

        """
        if not web_element:
            return (
                self.driver.find_elements(By.CLASS_NAME, name)
                if array
                else self.driver.find_element(By.CLASS_NAME, name)
            )
        else:
            return (
                web_element.find_elements(By.CLASS_NAME, name)
                if array
                else web_element.find_element(By.CLASS_NAME, name)
            )

    def find_by_css(self, value: str, web_element: WebElement) -> WebElement:
        """
        Returns a WebElement matching the value
        """
        return web_element.find_element(By.CSS_SELECTOR, value=value)

    def find_by_id(self, value: str) -> WebElement:
        """
        Returns a WebElement matching the value
        """
        return self.driver.find_element(By.ID, value=value)

    def find_by_tag(
        self, name: str, web_element: WebElement = None, array: bool = True
    ):
        """
        Returns the WebElement(s) that are children of the web_element passed in parameters
        If no children is given, then the full page will be searched\n
        If array is True then it will return all the matching elements
        Else only the first

        """
        if not web_element:
            return (
                self.driver.find_elements(By.TAG_NAME, name)
                if array
                else self.driver.find_element(By.TAG_NAME, name)
            )
        else:
            return (
                web_element.find_elements(By.TAG_NAME, name)
                if array
                else web_element.find_element(By.TAG_NAME, name)
            )

    def execute_script(self, script: str, web_element: WebElement = None):
        """
        Synchronously Executes JavaScript in the current window/frame.
        """
        return self.driver.execute_script(script, web_element)

    def move_to_element_click(self, web_element: WebElement):
        """
        Moves the mouse to a given WebElement and perform a click
        """
        return (
            self.action_chains.move_to_element(web_element).click(web_element).perform()
        )
