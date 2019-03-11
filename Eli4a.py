# answer1
from selenium import webdriver

# driver = webdriver.Chrome(executable_path='C:\\Users\\User\\Documents\\chromedriver.exe')
# driver.get('https://www.walla.co.il/')

driver = webdriver.Firefox(executable_path='C:\\Users\\User\\Documents\\geckodriver.exe')
driver.get('https://www.ynet.co.il/')
# answer2
driver.implicitly_wait(20)

title = driver.title
print("Web Title is:" + driver.title)
driver.refresh()
my_url = driver.title
if my_url == driver.title:
    print("Website is equal")
# answer3
# they are the same - yes
# answer4
driver.get('https://translate.google.com')
driver.find_element_by_id('source').send_keys("בית")
driver.find_element_by_id("source").click()
# Answer5
driver.get('https://www.youtube.com')
driver.find_element_by_id('search').click()
driver.find_element_by_id("search").send_keys("its my life")
driver.find_element_by_id("search").click()
# Answer6
driver.get('https://translate.google.com')
a = driver.find_element_by_id("gb")
b = driver.find_element_by_class_name("sl-sugg")
c = driver.find_element_by_xpath("//*[@id='sugg-item-en']")
print(a)
print(b)
print(c)
# Answer7
driver.get("https://www.facebook.com/")
driver.find_element_by_id("email").send_keys("elibonneh@gmail.com")
driver.find_element_by_id("pass").send_keys("1234567890")
