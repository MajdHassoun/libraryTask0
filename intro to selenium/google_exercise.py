from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
search_input = driver.find_element(By.ID, "APjFqb")
search_input.send_keys("programming")
search_input.send_keys(Keys.RETURN)

second_res = driver.find_element(By.CSS_SELECTOR, "h3")

print(second_res.text)
driver.quit()
