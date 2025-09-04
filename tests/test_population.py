import pytest
import time
from pages.population_page import PopulationPage

@pytest.mark.population
def test_extract_population(driver):
    page = PopulationPage(driver)
    page.load()

    print("\n--- World Population Clock ---")
    print("Press Command (⌘) + C to stop.\n")

    try:
        while True:
            count = page.get_population()
            print(f"Current Population: {count}")
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nStopped population tracking by user.")
