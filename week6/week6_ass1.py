from selenium import webdriver
import time

driver = webdriver.Chrome("./chromedriver")
driver.get("https://nid.naver.com")

login = driver.find_element_by_css_selector("input#id")
login.send_keys("joohee1026")
psswd = driver.find_element_by_css_selector("input#pw")
psswd.send_keys("rhdqngo3356%")
button = driver.find_element_by_css_selector('input.btn_global')
button.click()

driver2 = webdriver.Chrome("./chromedriver")
driver2.get("https://www.facebook.com/")
flogine = driver2.find_element_by_css_selector("input#email")
flogine.send_keys("joohee1026@naver.com")
fpasswd = driver2.find_element_by_css_selector("input#pass")
fpasswd.send_keys("rhdqngo3356%")
button2 = driver2.find_element_by_css_selector("label.login_form_login_button")
button2.click()
