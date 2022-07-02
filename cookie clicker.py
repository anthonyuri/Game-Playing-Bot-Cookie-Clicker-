from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import *

chrome_driver_path = "C:\Development/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")


cookie = driver.find_element(By.ID, "cookie")

timeout = time() + 5

store = driver.find_elements(By.CSS_SELECTOR, "#store div")

item_ids = [item.get_attribute("id")for item in store[:-1]]
print(item_ids)

item_prices = [int(item.find_element(By.CSS_SELECTOR, "b").text.split(" - ")[1].replace(",", "")) for item in store[:-1]]

print(item_prices)


while True:

    cookie.click()

    if time() > timeout:
        total_cookies = int(driver.find_element(By.ID, "money").text.replace(",", ""))
        print(total_cookies)

        highest = 0
        for price in item_prices:
            if total_cookies >= price and price >= highest:
                highest = price

        index = item_prices.index(highest)
        highest_id = item_ids[index]
        highest_item = driver.find_element(By.ID, highest_id)
        highest_item.click()


        timeout = time() + 5

