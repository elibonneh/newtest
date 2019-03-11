from selenium import webdriver

driver = webdriver.Firefox(executable_path='C:\\Users\\User\\Documents\\geckodriver.exe')

# driver.get('https://www.youtube.com/')
driver.get('https://www.google.co.il')
print(driver.current_url)
my_url = driver.current_url
driver.close()



# driver = webdriver.Firefox(executable_path='C:\\Users\\User\AppData\Local\Temp\geckodriver-v0.24.0-win64')
# driver.get('http://inventwithpython.com')