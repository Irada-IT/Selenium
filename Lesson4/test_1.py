from testpage import OperationsHelper
import logging
import time

def test_step1(browser):
    logging.info("Test 1 Start")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"
def test_step2(browser):
    logging.info("Test 2 Start")
    testpage = OperationsHelper(browser)
    testpage.enter_login("testtest1")
    testpage.enter_pass("c23b2ed66e")
    testpage.click_login_button()
    assert testpage.get_user_text() == "Hello, testtest1"
def test_step3(browser):
    logging.info("Test 3 Start")
    testpage = OperationsHelper(browser)
    testpage.click_new_post_btn()
    testpage.enter_title("Post1")
    testpage.enter_description("Description")
    testpage.enter_content("Content")
    testpage.click_save_btn()
    time.sleep(5)
    assert testpage.get_res_text() == "Post1"
def test_step4(browser):
    logging.info("Test 4 Start")
    testpage = OperationsHelper(browser)
    testpage.click_contact_btn()
    time.sleep(2)
    testpage.enter_name("testtest1")
    testpage.enter_email("test@mail.ru")
    testpage.enter_content2("Anything")
    time.sleep(2)
    testpage.click_contactus_btn()
    time.sleep(2)
    assert testpage.get_alert() == "Form successfully submitted"
