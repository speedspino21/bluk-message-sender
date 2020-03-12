# from lxml.html import fromstring
import requests
# from threading import Thread
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

from itertools import cycle

from random import randint
import datetime
import time

print('Loading-------')
currentDT = datetime.datetime.now()
print('current date:' + str(currentDT))

phones = []
r_phones = open('testphones.txt', 'r')
for r_phone in r_phones:
    each_phone = r_phone[0:len(r_phone)]
    if each_phone[-1] == "\n":
    	each_phone = r_phone[0:len(r_phone)-1]
    else:
        each_phone = r_phone[0:len(r_phone)]

    phones.append(re.findall(r'\d+', each_phone)[0])
print(phones)

message = ""
r_message = open('Message_text.txt', 'r')
for mes in r_message:
    message = mes
    if message[-1] == "\n":
        message = message[:-1]
r_message.close()
print(message)

driver = webdriver.Chrome()

# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--ignore-ssl-errors')
# driver = webdriver.Chrome(chrome_options=options)


driver.set_window_size(1400, 1000)

driver.get("https://zadarma.com/en/")

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-empty auth-button']")))

driver.find_element_by_xpath("//button[@class='btn btn-empty auth-button']").click()

driver.find_element_by_xpath("//div[@class='row header-top-line']/div[2]/div[2]/div/form/div[1]/input[@class='m-input'][@name='email']").send_keys("support1@hmrconstruction.co.uk")

driver.find_element_by_xpath("//div[@class='row header-top-line']/div[2]/div[2]/div/form/div[2]/input[@class='m-input'][@name='password']").send_keys("Damland420")

driver.find_element_by_xpath("//div[@class='row header-top-line']/div[2]/div[2]/div/form/button[@type='submit']").click()
time.sleep(1)
driver.get("https://my.zadarma.com/connect/sms/")
time.sleep(1)

for phone in phones:

	print ("-----" + phone + "-----")
	try:
		driver.find_element_by_xpath("//div[@class='smsform']/form/div[@id='numbers_adding']/div/input[@id='number1']").send_keys('')
		driver.find_element_by_xpath("//textarea[@id='message']").send_keys('')
		
		driver.find_element_by_xpath("//div[@class='smsform']/form/div[@id='numbers_adding']/div/input[@id='number1']").send_keys(phone)

		driver.find_element_by_xpath("//select[@id='caller_id']/option[@value='441450812518']").click()

		driver.find_element_by_xpath("//textarea[@id='message']").send_keys(message)
		
		time.sleep(1)
		send_button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='sendsms_btn']")))
		send_button.click()
		time.sleep(1)
		# driver.find_element_by_xpath("//input[@id='sendsms_btn']").click()
		
		# driver.get("https://my.zadarma.com/connect/sms/")

		print('success')
	except Exception as e:
		print('next')
		driver.find_element_by_xpath("//div[@class='smsform']/form/div[@id='numbers_adding']/div/input[@id='number1']").send_keys('')
		driver.find_element_by_xpath("//textarea[@id='message']").send_keys('')
		pass


print("END")

driver.close()





