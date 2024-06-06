from Lesson4.testpage2 import OperationsHelper
import logging


def test_step5(browser):
    logging.info("Test 5 Start")
    testpage2 = OperationsHelper(browser)
    assert testpage2.get_check_text() == None
