from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging

class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, """button""")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_HELLO = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/a""")
    LOCATOR_NEW_POST_BTN = (By.CSS_SELECTOR, "#create-btn")
    LOCATOR_TITLE = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    LOCATOR_DESCRIPTION = (By.XPATH, """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""")
    LOCATOR_CONTENT = (By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")
    LOCATOR_SAVE_BTN = (By.CSS_SELECTOR, """#create-item > div > div > div:nth-child(7) > div > button > span""")
    LOCATOR_RES_TEXT = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
    LOCATOR_CONTACT_BTN = (By.CSS_SELECTOR, """#app > main > nav > ul > li:nth-child(2) > a""")
    LOCATOR_NAME = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_EMAIL = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_CONTENT2 = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACTUS_BTN = (By.CSS_SELECTOR, """#contact > div.submit > button > span""")
class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)
    def enter_pass(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)
    def click_login_button(self):
        logging.info(f"Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=3)
        text = error_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return text
    def get_user_text(self):
        user_field = self.find_element(TestSearchLocators.LOCATOR_HELLO, time=2)
        text = user_field.text
        return text
    def click_new_post_btn(self):
        self.find_element(TestSearchLocators.LOCATOR_NEW_POST_BTN).click()
    def enter_title(self, word):
        login_field = self.find_element(TestSearchLocators.LOCATOR_TITLE)
        login_field.clear()
        login_field.send_keys(word)
    def enter_description(self, word):
        login_field = self.find_element(TestSearchLocators.LOCATOR_DESCRIPTION)
        login_field.clear()
        login_field.send_keys(word)
    def enter_content(self, word):
        login_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT)
        login_field.clear()
        login_field.send_keys(word)
    def click_save_btn(self):
        self.find_element(TestSearchLocators.LOCATOR_SAVE_BTN).click()

    def get_res_text(self):
        login_field = self.find_element(TestSearchLocators.LOCATOR_RES_TEXT, time=2)
        text = login_field.text
        return text
    def click_contact_btn(self):
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_BTN).click()
    def enter_name(self, word):
        login_field = self.find_element(TestSearchLocators.LOCATOR_NAME)
        login_field.clear()
        login_field.send_keys(word)
    def enter_email(self, word):
        login_field = self.find_element(TestSearchLocators.LOCATOR_EMAIL)
        login_field.clear()
        login_field.send_keys(word)
    def enter_content2(self, word):
        login_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT2)
        login_field.clear()
        login_field.send_keys(word)
    def click_contactus_btn(self):
        self.find_element(TestSearchLocators.LOCATOR_CONTACTUS_BTN).click()
    def get_alert_msg(self):
        alert = self.driver.switch_to.alert()
        text = alert.text
        return text

