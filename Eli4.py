# class 4 - Selenium נועד לבדיקות של אתרים
# CSS קובץ עיצוב

from selenium import webdriver

driver = webdriver.Firefox(executable_path='C:\\Users\\User\\Documents\\geckodriver.exe')
driver.implicitly_wait(5)

# driver.get('https://www.youtube.com/')
www.print(driver.current_url)
print("Web Title is:" + driver.title)
my_url = driver.current_url
# find element alt+shift+C
driver.find_element_by_id("gb")
element = driver.find_elements_by_name("tag")

# ניתן להשתמש באחד מהשורות הבאות לאותה מטרה של לחיצה על כפתור
driver.find_element_by_id("source").click()
driver.find_element_by_id('source').send_keys("hello")
# driver.find_element_by_id('source').clear()
my_button = driver.find_element_by_id("source")
print(my_button.is_displayed())

# my_list = driver.find_elements_by_id('source')
# my_list[0].click()

# textarea אלמנט שיודע לקבל אליו טקסט
from selenium.webdriver.common.keys import Keys
driver.find_element_by_id("source").send_keys(Keys.ENTER)
driver.find_element_by_id("source").send_keys(Keys.ENTER)




# driver.close()
# driver.quit()
