from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.instagram.com/explore/tags/ootd/")

pictures = driver.find_elements_by_css_selector("div._9AhH0")
time.sleep(3)

for picture in pictures:
    picture.click()
    time.sleep(2)
    try:
        contents = driver.find_element_by_css_selector("div.C4VMK span")
        print(contents.text)
    except:
        contents = '본문없음'
    time.sleep(2)
    close = driver.find_element_by_css_selector("button.ckWGn")
    close.click()

driver.close()


