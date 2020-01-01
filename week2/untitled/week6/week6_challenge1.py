from selenium import webdriver
import time

driver = webdriver.Chrome("./chromedriver")
driver.get("https://papago.naver.com")

time.sleep(0.5)

text_box = driver.find_element_by_css_selector("textarea#txtSource")
text_box.send_keys("seize the day")
btn = driver.find_element_by_css_selector("button#btnTranslate")
btn.click()

time.sleep(1)
result = driver.find_element_by_css_selector("div#txtTarget").text
print(result)

driver.close()
