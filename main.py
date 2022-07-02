from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\Development/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.python.org/")

# search_bar = driver.find_element(By.NAME, "q")
# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# jobs_link = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[1]/div[4]/p[2]/a')
# print(documentation_link.text)
# print(logo.size)
# print(jobs_link.text)

# menu = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div')
#
# menu_items = menu.text.splitlines()[2:]
# print(menu_items)

date_menu = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
dates = [element.text for element in date_menu]

event_menu = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events = [element.text for element in event_menu]

c = 0
nested_dict = {}
for date in dates:
    nested_dict[c] = {
        "time": date,
        "name": events[c]
    }
    c += 1

print(nested_dict)


# driver.close()
driver.quit()
