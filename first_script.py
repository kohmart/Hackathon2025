from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://cloudalm.cz")

title = driver.title
print(title)