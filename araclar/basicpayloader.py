from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Firefox()

browser.get('https://www.google.com/')

time.sleep(1)
#https://selenium-python.readthedocs.io/locating-elements.html#locating-by-name
form = browser.find_element(By.NAME, 'q')
#xss-payload-list.txt  ,sql-payload-list.txt  değiştirerek kullanabilirsiniz
dosya = open('xss-payload-list.txt ','r')
time.sleep(1)
for sifre in dosya:
    form.send_keys(sifre)
    print(sifre)
    form.send_keys(Keys.RETURN)
    time.sleep(1)
    browser.find_element(By.NAME, 'form_name').clear()
    #element.submit()

dosya.close()
