from selenium import webdriver
from time import sleep

# download correct version of chrome driver
# use full path
# pip install selenium in the environment created, make sure to activate the environment (venv not conda)
def open_page():
    # 'C:/Users/pragn/PycharmProjects/InstaBot/chromedriver_win32/chromedriver.exe'
    driver = webdriver.Chrome('C:/Users/pragn/PycharmProjects/InstaBot/chromedriver_win32/chromedriver.exe') #opens window
    return driver

def login(driver):
    driver.get("https://instagram.com")
    user_name = 'coder__123'
    pwd = 'ilovecoding'
    sleep(5) #IMPORTANT TO LOAD BEFORE LOGGING IN, could depend on wifi speed
    driver.find_element_by_xpath\
        ('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input').send_keys(user_name)
    driver.find_element_by_xpath\
        ('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input').send_keys(pwd)
    driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]').click()
    driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div') \
                .click()

def follow(driver, user):
    user_page = "https://instagram.com" + user
    driver.get(user_page)
    sleep(5)
    driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[2]/div/div/div/button')\
        .click()

driver = open_page()
login(driver)
sleep(1)
user = "/billnye/"
follow(driver, user)




#     user_name = 'coder__123'
#     pwd = 'ilovecoding'
#     sleep(5) #IMPORTANT TO LOAD BEFORE LOGGING IN, could depend on wifi speed
#     driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')\
#         .send_keys(user_name)
#     driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')\
#         .send_keys(pwd)
#     driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div')\
#         .click()
#     sleep(3)
#     if (driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')):
#         driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
#
# def follow(driver, user):
#     user_page = "https://instagram.com" + user
#     driver.get(user_page)
#     sleep(5)
#     driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[2]/div/div/div/button')\
#         .click()