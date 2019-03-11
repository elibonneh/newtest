from selenium import webdriver
driver = webdriver.Firefox(executable_path='C:\\Users\\User\\Documents\\geckodriver.exe')
driver.implicitly_wait(20)

driver.get('https://www.youtube.com')
driver.find_element_by_id('search').click()
driver.find_element_by_id('search').send_keys("its my life")
driver.find_element_by_id('search-icon-legacy').click()
