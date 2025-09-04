from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class PopulationPage:
    # Updated XPath: The population number is inside a span within "population_clock"
    POPULATION_COUNT = (By.XPATH, "//div[@id='population_clock']//h2")

    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.url = "https://www.theworldcounts.com/challenges/planet-earth/state-of-the-planet/world-population-clock-live"

    def load(self):
        self.driver.get(self.url)
        # Wait until at least one odometer digit is visible
        self.wait.until(EC.visibility_of_element_located(self.POPULATION_COUNT))

    def get_population(self):
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.POPULATION_COUNT))
            return element.text.strip()
        except TimeoutException:
            return "N/A"
