from BaseApp2 import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml

class TestSearchLocators:
    ids = dict()
    with open("locators2.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])


class OperationsHelper(BasePage):
    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while getting text from {element_name}")
            return None
        logging.debug(f"We find text {text} in field {element_name}")
        return text

    def get_check_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_POST_EXISTENCE"], description="check text")