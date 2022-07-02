from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()

wikipedia = driver.find_element(By.LINK_TEXT, "Wikipedia")
# all_portals.click()

search = driver.find_element(By.NAME, "search")

search.send_keys("Python")
search.send_keys(Keys.ENTER)





