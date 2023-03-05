from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("/Users/carlosfresnillo/Development/chromedriver")
driver = webdriver.Chrome(service=service)  # create Chrome driver obj, insert path

#  note: when a driver is done with all of its tasks it will close
driver.get("https://www.google.com")

driver.close()  # close current tab
driver.quit()  # quit program entirely
