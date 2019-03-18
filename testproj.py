from selenium import webdriver

driver = webdriver.Firefox(executable_path='C:\\Users\\User\\Documents\\geckodriver.exe')
driver.get('https://www.buyme.co.il/')
driver.implicitly_wait(20)
import time
time.sleep(5)

# Home Screen:

driver.find_element_by_id("ember664_chosen").click()
driver.find_element_by_xpath("//li[@data-option-array-index='2']").click()
driver.find_element_by_id("ember679_chosen").click()
driver.find_element_by_xpath("//li[@data-option-array-index='2']").click()
driver.find_element_by_id("ember688_chosen").click()
driver.find_element_by_xpath("//li[@data-option-array-index='3']").click()
driver.find_element_by_class_name("ui-btn").click()

# 3333333
import time
time.sleep(5)
driver.find_elements_by_class_name("card-item")[3].click()
driver.find_element_by_xpath("//div/div[2]/span").click()
driver.find_element_by_id('ember1669').send_keys("500")
driver.find_element_by_xpath("//form/div[2]/div/button").click()


# 44444:
driver.find_element_by_id('ember1303').send_keys("Dana")
driver.find_element_by_id('ember1305').send_keys("Eli")
driver.find_element_by_id('ember1323').send_keys("HAPPY BIRTHDAY")
driver.find_element_by_id('ember1332').click()
# driver.execute_script("arguments[0].click();", driver.find_element_by_class_name("ui-file"))

#
#  



