from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.youtube.com")
time.sleep(5)

popular = driver.find_elements_by_css_selector("paper-item.style-scope")
popular[1].click()

