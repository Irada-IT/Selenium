import yaml
from module import Site

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
site = Site(testdata["address"])

def test_step1(x_selector1, x_selector2, x_selector3, btn_selector, er1):
    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys("test")
    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys("test")
    btn = site.find_element("css", btn_selector)
    btn.click()
    err_label = site.find_element("xpath", x_selector3)
    text = err_label.text
    assert text == er1

def test_step2(x_selector1, x_selector2, x_selector4, btn_selector, er2):
    input1 = site.find_element("xpath", x_selector1)
    input1.clear()
    input1.send_keys("testtest1")
    input2 = site.find_element("xpath", x_selector2)
    input2.clear()
    input2.send_keys("c23b2ed66e")
    btn = site.find_element("css", btn_selector)
    btn.click()
    user_label = site.find_element("xpath", x_selector4)
    text = user_label.text
    assert text == er2
def test_step3(btn_selector2, x_selector5, x_selector6, x_selector7, btn_selector3, x_selector8, er3):
    btn2 = site.find_element("css", btn_selector2)
    btn2.click()
    input3 = site.find_element("xpath", x_selector5)
    input3.send_keys("Post1")
    input4 = site.find_element("xpath", x_selector6)
    input4.send_keys("Description")
    input5 = site.find_element("xpath", x_selector7)
    input5.send_keys("Content")
    btn3 = site.find_element("css", btn_selector3)
    btn3.click()
    post_label = site.find_element("xpath", x_selector8)
    text = post_label.text
    assert text == er3









