from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="C:\\Users\\bharath\\Documents\\drivers\\chrome.exe")
driver.get("https://www.youtube.com/")

driver.find_element_by_id("search").send_keys("Pattali makkal katchi")
driver.sleep(2)


