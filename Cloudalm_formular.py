from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://cloudalm.cz/formular/")

title = driver.title
print(title)
 
driver.implicitly_wait(5)

year = driver.find_element(by=By.ID, value="wpforms-19-field_1")
year.send_keys("2025")

manufacturer = driver.find_element(by=By.ID, value="wpforms-19-field_2")
manufacturer.send_keys("Škoda")

model = driver.find_element(by=By.NAME, value="wpforms[fields][3]")
model.send_keys("Superb")

vin = driver.find_element(by=By.NAME, value="wpforms[fields][4]")
vin.send_keys("1KZ12345678901234")

name = driver.find_element(by=By.NAME, value="wpforms[fields][8][first]")
name.send_keys("Jan")

surname = driver.find_element(by=By.NAME, value="wpforms[fields][8][last]")
surname.send_keys("Novák")

email = driver.find_element(by=By.NAME, value="wpforms[fields][7]")
email.send_keys("kohlik.m@seznam.cz")

kilometers = driver.find_element(by=By.NAME, value="wpforms[fields][5]")
kilometers.send_keys("100000")

average = driver.find_element(by=By.NAME, value="wpforms[fields][6]")
average.send_keys("5.5")

# submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
submit_button = driver.find_element(by=By.XPATH, value="//button[@type='submit']")
submit_button.click()

# message_div = driver.find_elements(by=By.ID, value="wpforms-confirmation-19")
# print(message_div.text)

divs = driver.find_elements(By.TAG_NAME, 'div')
print("Divů: ", len(divs))

paragraphs = driver.find_elements(By.TAG_NAME, 'p')
for paragraph in paragraphs:
    print(paragraph.text)

driver.quit()