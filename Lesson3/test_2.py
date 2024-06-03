from testpage import OperationsHelper
import logging
import time
def test_step1(browser):
    logging.info("Test2 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"
def test_step2(browser):
    testpage = OperationsHelper(browser)
    testpage.enter_login("testtest1")
    testpage.enter_pass("c23b2ed66e")
    testpage.click_login_button()
    assert testpage.get_user_text() == "Hello, testtest1"
#def test_step3(browser):
    #testpage = OperationsHelper(browser)
    #testpage.click_new_post_btn()
    #testpage.enter_title("Post1")
    #testpage.enter_description("Description")
    #testpage.enter_content("Content")
    #testpage.click_save_btn()
    #time.sleep(2)
    #assert testpage.get_res_text() == "Create Post"
def test_step4(browser):
    testpage = OperationsHelper(browser)
    testpage.click_contact_btn()
    testpage.enter_name("testtest1")
    testpage.enter_email("test@mail.ru")
    testpage.enter_content2("Anything")
    testpage.click_contactus_btn()
    time.sleep(2)
    assert testpage.get_alert_msg()