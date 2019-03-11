
from selenium import webdriver
driver = webdriver.Firefox(executable_path='C:\\Users\\User\\Documents\\geckodriver.exe')
driver.get('https://www.buyme.co.il/')
driver.implicitly_wait(20)
# Registration screen:
driver.find_element_by_class_name('seperator-link').click()
driver.find_element_by_class_name('text-btn').click()
driver.find_element_by_id('ember1019').send_keys("Eli")
driver.find_element_by_id('ember1021').send_keys("e134@gmail.com")
driver.find_element_by_id('valPass').send_keys("12345AAaa")
driver.find_element_by_id('ember1025').send_keys("12345AAaa")
driver.find_element_by_id("ember1028-id").click()
driver.execute_script("arguments[0].click();", driver.find_element_by_class_name("fa-check"))
driver.find_element_by_xpath("//div[3]/form/button").click()

# Home Screen:
driver.find_element_by_id("ember664_chosen").click()
driver.find_element_by_xpath("//li[@data-option-array-index='2']").click()
driver.find_element_by_id("ember679_chosen").click()
driver.find_element_by_xpath("//li[@data-option-array-index='2']").click()
driver.find_element_by_id("ember688_chosen").click()
driver.find_element_by_xpath("//li[@data-option-array-index='3']").click()
driver.find_element_by_class_name("ui-btn").click()

# Choose business screen:
import time
time.sleep(5)
driver.find_elements_by_class_name("card-item")[2].click()
driver.find_element_by_id('ember1199').send_keys("500")
driver.find_element_by_xpath("//div/button").click()

# Sender & Receiver information screen:
driver.find_element_by_id('ember1303').send_keys("Dana")
driver.find_element_by_id('ember1305').send_keys("Eli")
driver.find_element_by_id('ember1323').send_keys("HAPPY BIRTHDAY")
driver.find_element_by_id('ember1332').click()
driver.execute_script("arguments[0].click();", driver.find_element_by_class_name("ui-file"))



