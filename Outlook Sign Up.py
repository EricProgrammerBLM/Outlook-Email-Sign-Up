from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import string_utils
from selenium.webdriver.support.ui import Select
import random
from time import sleep

username = 'igmarketor847'
username = string_utils.shuffle(username)
username = 'a' + username
months = [1, 2, 3, 4, 5, 6 ,7 ,8 ,9 ,10, 11, 12]
random.shuffle(months)
days = [1, 3, 6, 12, 16, 20, 25, 26, 2]
random.shuffle(days)

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://signup.live.com/newuser.aspx?wa=wsignin1.0&rpsnv=13&ct=1618727206&rver=6.7.6631.0&wp=MBI_SSL&wreply=https%3a%2f%2fwww.bing.com%2fsecure%2fPassport.aspx%3frequrl%3dhttps%253a%252f%252fwww.bing.com%252f%253ftoWww%253d1%2526redig%253dE4FB33CBDAF74209A1612B26B6B4479F%2526wlexpsignin%253d1%26sig%3d288903D0CA686278209013CDCB0A633A&id=264960&CSRFToken=74d5019f-7eb0-4ab3-aae8-2989da7b06cb&aadredir=1&contextid=A34663E86ABA02E6&bk=1618727206&uiflavor=web&lic=1&mkt=EN-US&lc=1033&uaid=412e188e23334594ad53f1a33880cf67')
driver.find_element_by_id('liveSwitch').click()
driver.find_element_by_name('MemberName').send_keys(username)
driver.find_element_by_id('iSignupAction').click()
driver.implicitly_wait(20)
driver.find_element_by_id('PasswordInput').send_keys('goGetem837') #Password
driver.find_element_by_id('iSignupAction').click()
driver.implicitly_wait(20)
driver.find_element_by_name('FirstName').send_keys('John')
driver.find_element_by_name('LastName').send_keys('Doe')
driver.find_element_by_id('iSignupAction').click()
driver.implicitly_wait(20)

#Choosing Birth Month
opt = driver.find_element_by_xpath('//*[@id="BirthMonth"]')
dropdown = Select(opt)
dropdown.select_by_index(months[0])
#Choosing Birth Day
opt = driver.find_element_by_xpath('//*[@id="BirthDay"]')
dropdown = Select(opt)
dropdown.select_by_index(days[0])
#Typing in Birth Year
driver.find_element_by_xpath('//*[@id="BirthYear"]').send_keys(1996)
driver.find_element_by_id('iSignupAction').click()
while True:
	if driver.title == 'Bing':
		print (username + '@outlook.com')
		driver.get('https://outlook.live.com/mail/0/inbox')
		sleep(3000)
	else:
		sleep(5)

