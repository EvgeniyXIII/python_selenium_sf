# python -m pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome("/Users/User/projects/python_selenium_sf/chromdriver")
# driver.get("https://google.com")
driver.get("https://www.pitomec.ru/")
driver.save_screenshot("sf.png")
# driver.find_element(By.XPATH, "//*[@id=\"lightbox-nav\"]").send_keys("Skillfactiry" + Keys.RETURN)
t = driver.find_element(By.XPATH, "//*[@id=\"lightbox-nav\"]")
# sleep(5)
# driver.save_screenshot("sf.png")
print(t)
driver.quit()
