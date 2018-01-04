#download chromedriver for chrome broweser
#https://sites.google.com/a/chromium.org/chromedriver/downloads
from selenium import webdriver
def open_the_fb():
    usr ="######"
    pwd ="######"
    driver = webdriver.Chrome('path/to/chromedriver.exe')
    driver.get('https://www.facebook.com/')
    print("Opened facebook")
    username_box = driver.find_element_by_id('email')
    username_box.send_keys(usr)
    print("Email Id entered")
    password_box = driver.find_element_by_id('pass')
    password_box.send_keys(pwd)
    print("Password entered")
    login_box = driver.find_element_by_id('loginbutton')
    login_box.click()
def close_fb():
    driver = webdriver.Chrome('E:/My_Projects/SpellAndGrammerChecker/chromedriver.exe')
    print('Sucessfully logout is done')
    driver.quit()
