from selenium import webdriver
import time

driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.google.com/maps")

time.sleep(5)

text_box = driver.find_element_by_css_selector("input#searchboxinput")
text_box.send_keys("카페")
button = driver.find_element_by_css_selector("button#searchbox-searchbutton")
button.click()

#container, name, score, address
time.sleep(5)

while(1):
    time.sleep(5)
    cafes = driver.find_elements_by_css_selector("div.section-result-text-content")
    for cafe in cafes:
        name = cafe.find_element_by_css_selector("h3.section-result-title").text
        try:
            score = cafe.find_element_by_css_selector("span.cards-rating-score").text  # except처리
        except:
            score = "점수정보 없음"
        address = cafe.find_element_by_css_selector("span.section-result-location").text
        print(name, score, address)
    try:
        next_button = driver.find_element_by_css_selector("button#n7lv7yjyC35__section-pagination-button-next")
        next_button.click()
    except:
        print("complete")
        break

