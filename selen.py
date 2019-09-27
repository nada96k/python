from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import csv

driver = webdriver.Chrome(r'C:\Users\Nosaiba Al-AbdulElah\PycharmProjects\selenium\driver\chromedriver.exe')

driver.set_page_load_timeout(10)
driver.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1569432466&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3dca0459c4-8dc6-766a-1f3f-6cdffa01a057&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015')
time.sleep(3)
driver.find_element_by_name('loginfmt').send_keys("nadawe_96@hotmail.com")
login_button = driver.find_element_by_id("idSIButton9")
login_button.click()
driver.find_element_by_name('passwd').send_keys("nka2141116244")
time.sleep(3)
c = driver.find_element_by_id("idSIButton9")
c.click()
time.sleep(10)
driver.find_element_by_name('رسالة جديدة').click()

li = []

with open ('mycsv.csv','r') as f:
    emaillist = csv.reader(f)

    for eml in emaillist:
        time.sleep(8)
        driver.find_element_by_class_name('ms-BasePicker-input').send_keys(eml)
        driver.find_element_by_class_name('ms-BasePicker-input').send_keys(',')


time.sleep(2)
driver.find_element_by_class_name('ms-TextField-field').send_keys('Test')


time.sleep(2)
driver.find_element_by_class_name('_4utP_vaqQ3UQZH0GEBVQe').send_keys('Hello There!')

time.sleep(2)
# Un-comment the line below if you really want to send the email :D
#driver.find_element_by_name('إرسال').click()

