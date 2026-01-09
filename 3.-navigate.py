from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.google.com")
ele = driver.find_element(By.NAME, "q")
ele.send_keys("Selenium")
ele.send_keys(Keys.ARROW_DOWN)
# ele.send_keys(Keys.RETURN)
input('Enter any key to close')
