# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support.ui import Select
import shutil, time

f = open('C:\\chrome\\logpass.txt', 'r')
accs = f.readlines()
f.close()
shutil.copytree("C:\\chrome\\Profile1", "C:\\chrome\\Profile-1Work")
shutil.copytree("C:\\chrome\\Profile1", "C:\\chrome\\Profile-2Work")
shutil.copytree("C:\\chrome\\Profile1", "C:\\chrome\\Profile-3Work")
shutil.copytree("C:\\chrome\\Profile1", "C:\\chrome\\Profile-4Work")
shutil.copytree("C:\\chrome\\Profile1", "C:\\chrome\\Profile-5Work")
shutil.copytree("C:\\chrome\\Profile1", "C:\\chrome\\Profile-6Work")
shutil.copytree("C:\\chrome\\Profile1", "C:\\chrome\\Profile-7Work")
shutil.copytree("C:\\chrome\\Profile1", "C:\\chrome\\Profile-8Work")
#HOOK for pop 
acc = accs.pop()

# CREATE CHROME 1
chrome_options = webdriver.ChromeOptions() 
chrome_options.add_argument("user-agent=firefox")
chrome_options.add_argument("user-data-dir=C:\\chrome\\Profile-1Work") 
driver = webdriver.Chrome(chrome_options=chrome_options) 
driver.set_page_load_timeout(120)
driver.get("http://www.gamdom.com")
result = ui.WebDriverWait(driver, 40).until(lambda driver: driver.find_element_by_id("welcomeDialogText")) 
driver.find_element_by_id("iAgree").click()
driver.find_elements(By.CSS_SELECTOR,"a.button.login.icon ")[0].click()
result = ui.WebDriverWait(driver, 40).until(lambda driver: driver.find_element_by_id("steamAccountName")) 
acc = accs.pop()
try:
    driver.find_element_by_id("steamAccountName").send_keys(acc.split(":")[0])
    driver.find_element_by_id("steamPassword").send_keys(acc.split(":")[1])
    driver.find_element_by_id("imageLogin").click()
except:
    print("some exception ")
chrome_options_mail = webdriver.ChromeOptions() 
chrome_options_mail.add_argument("user-agent=firefox")
driver_mail = webdriver.Chrome(chrome_options=chrome_options_mail) 
driver_mail.delete_all_cookies()
driver_mail.set_page_load_timeout(120) 
driver_mail.get("https://temp-mail.org/ru/option/change/")
###-
try:
	first_result = ui.WebDriverWait(driver_mail, 12).until(lambda driver_mail: driver_mail.find_element_by_name("mail"))
	driver_mail.find_element_by_name("mail").clear()
	driver_mail.find_element_by_name("mail").send_keys(acc.split(":")[2].split("@")[0])
	Select(driver_mail.find_element_by_id('domain')).select_by_visible_text("@zep-hyr.com")
	driver_mail.find_element_by_id("postbut").click()
	driver_mail.get("https://temp-mail.org/ru")
	ui.WebDriverWait(driver_mail, 50).until(lambda driver_mail: driver_mail.find_element_by_id("mails"))
	time.sleep(2)
	rows = driver_mail.find_elements(By.CSS_SELECTOR,"a.title-subject")
	for row in rows[::-1]:
		if (row.get_attribute("innerText")=="Your Steam account: Acces"):
			print("-- HAVE STEAM "+row.get_attribute("href"))
			driver_mail.get(row.get_attribute("href"))
			break
	ui.WebDriverWait(driver_mail, 50).until(lambda driver_mail: driver_mail.find_elements(By.CSS_SELECTOR,"div.mailView"))
	CODE = "NO"
	trs = driver_mail.find_elements(By.CSS_SELECTOR,"table")[1].find_elements(By.CSS_SELECTOR,"tr")
	for i, tr in enumerate(trs):
		if (tr.get_attribute('innerText').find("Here is the Steam Guard code you need to login to account")!=-1):
			CODE=trs[i+1].get_attribute('innerText')
			
	driver_mail.close()  
	driver.find_element_by_id("authcode").send_keys(CODE)   
	ui.WebDriverWait(driver, 20).until(lambda driver: driver.find_elements(By.CSS_SELECTOR,"#success_continue_btn"))
	time.sleep(3)
	driver.find_elements(By.CSS_SELECTOR,"#success_continue_btn")[0].click()  
	ui.WebDriverWait(driver, 20).until(lambda driver: driver.find_elements(By.CSS_SELECTOR,"#iAgree"))
	time.sleep(2)
	driver.find_elements(By.CSS_SELECTOR,"#iAgree")[0].click()  
	time.sleep(2)
	driver.find_elements(By.CSS_SELECTOR,"body > div.ReactModalPortal > div > div > div > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix > div > button")[0].click()  
	ui.WebDriverWait(driver, 20).until(lambda driver: driver.find_elements(By.CSS_SELECTOR,"i.visible-phone.fa.fa-gift"))
	time.sleep(2)
	driver.find_elements(By.CSS_SELECTOR,"i.visible-phone.fa.fa-gift")[0].click()
	try:
		ui.WebDriverWait(driver, 20).until(lambda driver: driver.find_elements(By.CSS_SELECTOR,"button.claimReward"))
		time.sleep(1)
		driver.find_elements(By.CSS_SELECTOR,"button.claimReward")[0].click()
		ui.WebDriverWait(driver, 20).until(lambda driver: driver.find_elements(By.CSS_SELECTOR,"button.claimRewardDisabled"))
		time.sleep(2)
		driver.find_elements(By.CSS_SELECTOR,"i.visible-phone.fa.fa-user-plus")[0].click()
		ui.WebDriverWait(driver, 20).until(lambda driver: driver.find_elements(By.CSS_SELECTOR,"#referral_code"))
		time.sleep(2)
		driver.find_elements(By.CSS_SELECTOR,"#referral_code")[0].send_keys("111111111122")
		time.sleep(3)
		driver.find_elements(By.CSS_SELECTOR,"#tabs-inner-container > div.widget-container.container-for-affiliate > div > div > div:nth-child(1) > button")[0].click()
		time.sleep(2)
		driver.find_elements(By.CSS_SELECTOR,"#tabs-inner-container > div.widget-container.container-for-affiliate > div > div > div:nth-child(1) > button")[0].click()
		time.sleep(2)
		driver.execute_script("arguments[0].scrollIntoView();", driver.find_elements(By.CSS_SELECTOR,"#tabs-inner-container > div.widget-container.container-for-affiliate > div > div > div.total-money > button")[0])
		time.sleep(2)
		driver.find_elements(By.CSS_SELECTOR,"#tabs-inner-container > div.widget-container.container-for-affiliate > div > div > div.total-money > button")[0].click()
		time.sleep(2)
		driver.find_elements(By.CSS_SELECTOR,"#tabs-inner-container > div.widget-container.container-for-affiliate > div > div > div.total-money > button")[0].click()
					
	except:
		print("exception")
except:
	print("exception")
    
#----------------------------------------------------------- CREATE CHROME 2
chrome_options2 = webdriver.ChromeOptions() 
chrome_options2.add_argument("user-agent=firefox")
chrome_options2.add_argument("user-data-dir=C:\\chrome\\Profile-2Work") 
driver2 = webdriver.Chrome(chrome_options=chrome_options2) 
driver2.set_page_load_timeout(120)
driver2.get("http://www.gamdom.com")
result = ui.WebDriverWait(driver2, 40).until(lambda driver2: driver2.find_element_by_id("welcomeDialogText")) 
driver2.find_element_by_id("iAgree").click()
driver2.find_elements(By.CSS_SELECTOR,"a.button.login.icon ")[0].click()
result = ui.WebDriverWait(driver2, 40).until(lambda driver2: driver2.find_element_by_id("steamAccountName")) 
acc = accs.pop()
try:
    driver2.find_element_by_id("steamAccountName").send_keys(acc.split(":")[0])
    driver2.find_element_by_id("steamPassword").send_keys(acc.split(":")[1])
    driver2.find_element_by_id("imageLogin").click()
except:
    print("some exception ")
chrome_options_mail2 = webdriver.ChromeOptions() 
chrome_options_mail2.add_argument("user-agent=firefox")
driver_mail2 = webdriver.Chrome(chrome_options=chrome_options_mail2) 
driver_mail2.delete_all_cookies()
driver_mail2.set_page_load_timeout(120) 
driver_mail2.get("https://temp-mail.org/ru/option/change/")
try:
	first_result = ui.WebDriverWait(driver_mail2, 12).until(lambda driver_mail2: driver_mail2.find_element_by_name("mail"))
	driver_mail2.find_element_by_name("mail").clear()
	driver_mail2.find_element_by_name("mail").send_keys(acc.split(":")[2].split("@")[0])
	Select(driver_mail2.find_element_by_id('domain')).select_by_visible_text("@zep-hyr.com")
	driver_mail2.find_element_by_id("postbut").click()
	driver_mail2.get("https://temp-mail.org/ru")
	ui.WebDriverWait(driver_mail2, 50).until(lambda driver_mail2: driver_mail2.find_element_by_id("mails"))
	time.sleep(2)
	rows = driver_mail2.find_elements(By.CSS_SELECTOR,"a.title-subject")
	for row in rows[::-1]:
		if (row.get_attribute("innerText")=="Your Steam account: Acces"):
			print("-- HAVE STEAM "+row.get_attribute("href"))
			driver_mail2.get(row.get_attribute("href"))
			break
	ui.WebDriverWait(driver_mail2, 50).until(lambda driver_mail2: driver_mail2.find_elements(By.CSS_SELECTOR,"div.mailView"))
	CODE = "NO"
	trs = driver_mail2.find_elements(By.CSS_SELECTOR,"table")[1].find_elements(By.CSS_SELECTOR,"tr")
	for i, tr in enumerate(trs):
		if (tr.get_attribute('innerText').find("Here is the Steam Guard code you need to login to account")!=-1):
			CODE=trs[i+1].get_attribute('innerText')
			
	driver_mail2.close()  
	driver2.find_element_by_id("authcode").send_keys(CODE)   
	ui.WebDriverWait(driver2, 20).until(lambda driver2: driver2.find_elements(By.CSS_SELECTOR,"#success_continue_btn"))
	time.sleep(3)
	driver2.find_elements(By.CSS_SELECTOR,"#success_continue_btn")[0].click()              
	ui.WebDriverWait(driver2, 20).until(lambda driver2: driver2.find_elements(By.CSS_SELECTOR,"#iAgree"))
	time.sleep(2)
	driver2.find_elements(By.CSS_SELECTOR,"#iAgree")[0].click()  
	time.sleep(2)
	driver2.find_elements(By.CSS_SELECTOR,"body > div.ReactModalPortal > div > div > div > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix > div > button")[0].click()  
	ui.WebDriverWait(driver2, 20).until(lambda driver2: driver2.find_elements(By.CSS_SELECTOR,"i.visible-phone.fa.fa-gift"))
	time.sleep(2)
	driver2.find_elements(By.CSS_SELECTOR,"i.visible-phone.fa.fa-gift")[0].click()
	try:
		ui.WebDriverWait(driver2, 20).until(lambda driver2: driver2.find_elements(By.CSS_SELECTOR,"button.claimReward"))
		time.sleep(1)
		driver2.find_elements(By.CSS_SELECTOR,"button.claimReward")[0].click()
		ui.WebDriverWait(driver2, 20).until(lambda driver2: driver2.find_elements(By.CSS_SELECTOR,"button.claimRewardDisabled"))
		time.sleep(2)
		driver2.find_elements(By.CSS_SELECTOR,"i.visible-phone.fa.fa-user-plus")[0].click()
		ui.WebDriverWait(driver2, 20).until(lambda driver2: driver2.find_elements(By.CSS_SELECTOR,"#referral_code"))
		time.sleep(2)
		driver2.find_elements(By.CSS_SELECTOR,"#referral_code")[0].send_keys("111111111122")
		time.sleep(3)
		driver2.find_elements(By.CSS_SELECTOR,"#tabs-inner-container > div.widget-container.container-for-affiliate > div > div > div:nth-child(1) > button")[0].click()
		time.sleep(2)
		driver2.find_elements(By.CSS_SELECTOR,"#tabs-inner-container > div.widget-container.container-for-affiliate > div > div > div:nth-child(1) > button")[0].click()
		time.sleep(2)
		driver2.execute_script("arguments[0].scrollIntoView();", driver2.find_elements(By.CSS_SELECTOR,"#tabs-inner-container > div.widget-container.container-for-affiliate > div > div > div.total-money > button")[0])
		time.sleep(1)                       
		driver2.find_elements(By.CSS_SELECTOR,"#tabs-inner-container > div.widget-container.container-for-affiliate > div > div > div.total-money > button")[0].click()
		time.sleep(2)
		driver2.find_elements(By.CSS_SELECTOR,"#tabs-inner-container > div.widget-container.container-for-affiliate > div > div > div.total-money > button")[0].click()
				 
	except:
		print("exception")   
except:
	print("exception") 		
	
#----------------------------------------------------------- CREATE CHROME 3
chrome_options23 = webdriver.ChromeOptions() 
chrome_options23.add_argument("user-agent=firefox")
chrome_options23.add_argument("user-data-dir=C:\\chrome\\Profile-3Work") 
driver23 = webdriver.Chrome(chrome_options=chrome_options23) 
driver23.set_page_load_timeout(120)
driver23.get("http://www.gamdom.com")
result = ui.WebDriverWait(driver23, 40).until(lambda driver23: driver23.find_element_by_id("welcomeDialogText")) 
driver23.find_element_by_id("iAgree").click()
driver23.find_elements(By.CSS_SELECTOR,"a.button.login.icon ")[0].click()
result = ui.WebDriverWait(driver23, 40).until(lambda driver23: driver23.find_element_by_id("steamAccountName")) 
acc = accs.pop()
try:
    driver23.find_element_by_id("steamAccountName").send_keys(acc.split(":")[0])
    driver23.find_element_by_id("steamPassword").send_keys(acc.split(":")[1])
    driver23.find_element_by_id("imageLogin").click()
except:
    print("some exception ")
chrome_options_mail23 = webdriver.ChromeOptions() 
chrome_options_mail23.add_argument("user-agent=firefox")
driver_mail23 = webdriver.Chrome(chrome_options=chrome_options_mail23) 
driver_mail23.delete_all_cookies()
driver_mail23.set_page_load_timeout(120) 
driver_mail23.get("https://temp-mail.org/ru/option/change/")
try:
	first_result = ui.WebDriverWait(driver_mail2, 12).until(lambda driver_mail2: driver_mail23.find_element_by_name("mail"))
	driver_mail23.find_element_by_name("mail").clear()
	driver_mail23.find_element_by_name("mail").send_keys(acc.split(":")[2].split("@")[0])
	Select(driver_mail23.find_element_by_id('domain')).select_by_visible_text("@zep-hyr.com")
	driver_mail23.find_element_by_id("postbut").click()
	driver_mail23.get("https://temp-mail.org/ru")
	ui.WebDriverWait(driver_mail23, 50).until(lambda driver_mail23: driver_mail23.find_element_by_id("mails"))
	time.sleep(2)
	rows = driver_mail23.find_elements(By.CSS_SELECTOR,"a.title-subject")
	for row in rows[::-1]:
		if (row.get_attribute("innerText")=="Your Steam account: Acces"):
			print("-- HAVE STEAM "+row.get_attribute("href"))
			driver_mail23.get(row.get_attribute("href"))
			break
	ui.WebDriverWait(driver_mail23, 50).until(lambda driver_mail23: driver_mail23.find_elements(By.CSS_SELECTOR,"div.mailView"))
	CODE = "NO"
	trs = driver_mail23.find_elements(By.CSS_SELECTOR,"table")[1].find_elements(By.CSS_SELECTOR,"tr")
	for i, tr in enumerate(trs):
		if (tr.get_attribute('innerText').find("Here is the Steam Guard code you need to login to account")!=-1):
			CODE=trs[i+1].get_attribute('innerText')
			
	driver_mail23.close()  
	driver23.find_element_by_id("authcode").send_keys(CODE)   
	ui.WebDriverWait(driver23, 20).until(lambda driver23: driver23.find_elements(By.CSS_SELECTOR,"#success_continue_btn"))
	time.sleep(3)
	driver23.find_elements(By.CSS_SELECTOR,"#success_continue_btn")[0].click()              
	ui.WebDriverWait(driver23, 20).until(lambda driver23: driver23.find_elements(By.CSS_SELECTOR,"#iAgree"))
	time.sleep(2)
	driver23.find_elements(By.CSS_SELECTOR,"#iAgree")[0].click()  
	time.sleep(2)
	driver23.find_elements(By.CSS_SELECTOR,"body > div.ReactModalPortal > div > div > div > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix > div > button")[0].click()  
	ui.WebDriverWait(driver23, 20).until(lambda driver23: driver23.find_elements(By.CSS_SELECTOR,"i.visible-phone.fa.fa-gift"))
	time.sleep(2)
	driver23.find_elements(By.CSS_SELECTOR,"i.visible-phone.fa.fa-gift")[0].click()
	try:
		ui.WebDriverWait(driver23, 20).until(lambda driver23: driver23.find_elements(By.CSS_SELECTOR,"button.claimReward"))
		time.sleep(1)
		driver23.find_elements(By.CSS_SELECTOR,"button.claimReward")[0].click()
		ui.WebDriverWait(driver23, 20).until(lambda driver23: driver23.find_elements(By.CSS_SELECTOR,"button.claimRewardDisabled"))
		time.sleep(2)
		driver23.find_elements(By.CSS_SELECTOR,"i.visible-phone.fa.fa-user-plus")[0].click()
		ui.WebDriverWait(driver23, 20).until(lambda driver23: driver23.find_elements(By.CSS_SELECTOR,"#referral_code"))
		time.sleep(2)
		driver23.find_elements(By.CSS_SELECTOR,"#referral_code")[0].send_keys("111111111122")
		time.sleep(3)
		driver23.find_elements(By.CSS_SELECTOR,"#tabs-inner-container > div.widget-container.container-for-affiliate > div > div > div:nth-child(1) > button")[0].click()
		time.sleep(2)
		driver23.find_elements(By.CSS_SELECTOR,"#tabs-inner-container > div.widget-container.container-for-affiliate > div > div > div:nth-child(1) > button")[0].click()
		time.sleep(2)
		driver23.execute_script("arguments[0].scrollIntoView();", driver23.find_elements(By.CSS_SELECTOR,"#tabs-inner-container > div.widget-container.container-for-affiliate > div > div > div.total-money > button")[0])
		time.sleep(1)                       
		driver23.find_elements(By.CSS_SELECTOR,"#tabs-inner-container > div.widget-container.container-for-affiliate > div > div > div.total-money > button")[0].click()
		time.sleep(2)
		driver23.find_elements(By.CSS_SELECTOR,"#tabs-inner-container > div.widget-container.container-for-affiliate > div > div > div.total-money > button")[0].click()
				 
	except:
		print("exception")     
except:
	print("exception")  
	
#----------------------------------------------------------- CREATE CHROME 4
chrome_options24 = webdriver.ChromeOptions() 
chrome_options24.add_argument("user-agent=firefox")
chrome_options24.add_argument("user-data-dir=C:\\chrome\\Profile-4Work") 
driver24 = webdriver.Chrome(chrome_options=chrome_options24) 
driver24.set_page_load_timeout(120)
driver24.get("http://www.gamdom.com")
result = ui.WebDriverWait(driver24, 40).until(lambda driver24: driver24.find_element_by_id("welcomeDialogText")) 
driver24.find_element_by_id("iAgree").click()
driver24.find_elements(By.CSS_SELECTOR,"a.button.login.icon ")[0].click()
result = ui.WebDriverWait(driver24, 40).until(lambda driver24: driver24.find_element_by_id("steamAccountName")) 
acc = accs.pop()
try:
    driver24.find_element_by_id("steamAccountName").send_keys(acc.split(":")[0])
    driver24.find_element_by_id("steamPassword").send_keys(acc.split(":")[1])
    driver24.find_element_by_id("imageLogin").click()
except:
    print("some exception ")
chrome_options_mail24 = webdriver.ChromeOptions() 
chrome_options_mail24.add_argument("user-agent=firefox")
driver_mail24 = webdriver.Chrome(chrome_options=chrome_options_mail24) 
driver_mail24.delete_all_cookies()
driver_mail24.set_page_load_timeout(120) 
driver_mail24.get("https://temp-mail.org/ru/option/change/")
try:
	first_result = ui.WebDriverWait(driver_mail2, 12).until(lambda driver_mail2: driver_mail24.find_element_by_name("mail"))
	driver_mail24.find_element_by_name("mail").clear()
	driver_mail24.find_element_by_name("mail").send_keys(acc.split(":")[2].split("@")[0])
	Select(driver_mail24.find_element_by_id('domain')).select_by_visible_text("@zep-hyr.com")
	driver_mail24.find_element_by_id("postbut").click()
	driver_mail24.get("https://temp-mail.org/ru")
	ui.WebDriverWait(driver_mail24, 50).until(lambda driver_mail24: driver_mail24.find_element_by_id("mails"))
	time.sleep(2)
	rows = driver_mail24.find_elements(By.CSS_SELECTOR,"a.title-subject")
	for row in rows[::-1]:
		if (row.get_attribute("innerText")=="Your Steam account: Acces"):
			print("-- HAVE STEAM "+row.get_attribute("href"))
			driver_mail24.get(row.get_attribute("href"))
			break
	ui.WebDriverWait(driver_mail24, 50).until(lambda driver_mail24: driver_mail24.find_elements(By.CSS_SELECTOR,"div.mailView"))
	CODE = "NO"
	trs = driver_mail24.find_elements(By.CSS_SELECTOR,"table")[1].find_elements(By.CSS_SELECTOR,"tr")
	for i, tr in enumerate(trs):
		if (tr.get_attribute('innerText').find("Here is the Steam Guard code you need to login to account")!=-1):
			CODE=trs[i+1].get_attribute('innerText')
			
	driver_mail24.close()  
	driver24.find_element_by_id("authcode").send_keys(CODE)   
	ui.WebDriverWait(driver24, 20).until(lambda driver24: driver24.find_elements(By.CSS_SELECTOR,"#success_continue_btn"))
	time.sleep(3)
	driver24.find_elements(By.CSS_SELECTOR,"#success_continue_btn")[0].click()              
	ui.WebDriverWait(driver24, 20).until(lambda driver24: driver24.find_elements(By.CSS_SELECTOR,"#iAgree"))
	time.sleep(2)
	driver24.find_elements(By.CSS_SELECTOR,"#iAgree")[0].click()  
	time.sleep(2)
	driver24.find_elements(By.CSS_SELECTOR,"body > div.ReactModalPortal > div > div > div > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix > div > button")[0].click()  
	ui.WebDriverWait(driver24, 20).until(lambda driver24: driver24.find_elements(By.CSS_SELECTOR,"i.visible-phone.fa.fa-gift"))
	time.sleep(2)
	driver24.find_elements(By.CSS_SELECTOR,"i.visible-phone.fa.fa-gift")[0].click()
	try:
		ui.WebDriverWait(driver24, 20).until(lambda driver24: driver24.find_elements(By.CSS_SELECTOR,"button.claimReward"))
		time.sleep(1)
		driver24.find_elements(By.CSS_SELECTOR,"button.claimReward")[0].click()
		ui.WebDriverWait(driver24, 20).until(lambda driver24: driver24.find_elements(By.CSS_SELECTOR,"button.claimRewardDisabled"))
		time.sleep(2)
		driver24.find_elements(By.CSS_SELECTOR,"i.visible-phone.fa.fa-user-plus")[0].click()
		ui.WebDriverWait(driver24, 20).until(lambda driver24: driver24.find_elements(By.CSS_SELECTOR,"#referral_code"))
		time.sleep(2)
		driver24.find_elements(By.CSS_SELECTOR,"#referral_code")[0].send_keys("111111111122")
		time.sleep(3)
		driver24.find_elements(By.CSS_SELECTOR,"#tabs-inner-container > div.widget-container.container-for-affiliate > div > div > div:nth-child(1) > button")[0].click()
		time.sleep(2)
		driver24.find_elements(By.CSS_SELECTOR,"#tabs-inner-container > div.widget-container.container-for-affiliate > div > div > div:nth-child(1) > button")[0].click()
		time.sleep(2)
		driver24.execute_script("arguments[0].scrollIntoView();", driver24.find_elements(By.CSS_SELECTOR,"#tabs-inner-container > div.widget-container.container-for-affiliate > div > div > div.total-money > button")[0])
		time.sleep(1)                       
		driver24.find_elements(By.CSS_SELECTOR,"#tabs-inner-container > div.widget-container.container-for-affiliate > div > div > div.total-money > button")[0].click()
		time.sleep(2)
		driver24.find_elements(By.CSS_SELECTOR,"#tabs-inner-container > div.widget-container.container-for-affiliate > div > div > div.total-money > button")[0].click()
				 
	except:
		print("exception")     
except:
	print("exception")    
	
#----------------------------------------------------------- CREATE CHROME 5
chrome_options25 = webdriver.ChromeOptions() 
chrome_options25.add_argument("user-agent=firefox")
chrome_options25.add_argument("user-data-dir=C:\\chrome\\Profile-5Work") 
driver25 = webdriver.Chrome(chrome_options=chrome_options25) 
driver25.set_page_load_timeout(120)
driver25.get("http://www.gamdom.com")
result = ui.WebDriverWait(driver25, 40).until(lambda driver25: driver25.find_element_by_id("welcomeDialogText")) 
driver25.find_element_by_id("iAgree").click()
driver25.find_elements(By.CSS_SELECTOR,"a.button.login.icon ")[0].click()
result = ui.WebDriverWait(driver25, 40).until(lambda driver25: driver25.find_element_by_id("steamAccountName")) 
acc = accs.pop()
try:
    driver25.find_element_by_id("steamAccountName").send_keys(acc.split(":")[0])
    driver25.find_element_by_id("steamPassword").send_keys(acc.split(":")[1])
    driver25.find_element_by_id("imageLogin").click()
except:
    print("some exception ")
chrome_options_mail25 = webdriver.ChromeOptions() 
chrome_options_mail25.add_argument("user-agent=firefox")
driver_mail25 = webdriver.Chrome(chrome_options=chrome_options_mail25) 
driver_mail25.delete_all_cookies()
driver_mail25.set_page_load_timeout(120) 
driver_mail25.get("https://temp-mail.org/ru/option/change/")
try:
	first_result = ui.WebDriverWait(driver_mail2, 12).until(lambda driver_mail2: driver_mail25.find_element_by_name("mail"))
	driver_mail25.find_element_by_name("mail").clear()
	driver_mail25.find_element_by_name("mail").send_keys(acc.split(":")[2].split("@")[0])
	Select(driver_mail25.find_element_by_id('domain')).select_by_visible_text("@zep-hyr.com")
	driver_mail25.find_element_by_id("postbut").click()
	driver_mail25.get("https://temp-mail.org/ru")
	ui.WebDriverWait(driver_mail25, 50).until(lambda driver_mail25: driver_mail25.find_element_by_id("mails"))
	time.sleep(2)
	rows = driver_mail25.find_elements(By.CSS_SELECTOR,"a.title-subject")
	for row in rows[::-1]:
		if (row.get_attribute("innerText")=="Your Steam account: Acces"):
			print("-- HAVE STEAM "+row.get_attribute("href"))
			driver_mail25.get(row.get_attribute("href"))
			break
	ui.WebDriverWait(driver_mail25, 50).until(lambda driver_mail25: driver_mail25.find_elements(By.CSS_SELECTOR,"div.mailView"))
	CODE = "NO"
	trs = driver_mail25.find_elements(By.CSS_SELECTOR,"table")[1].find_elements(By.CSS_SELECTOR,"tr")
	for i, tr in enumerate(trs):
		if (tr.get_attribute('innerText').find("Here is the Steam Guard code you need to login to account")!=-1):
			CODE=trs[i+1].get_attribute('innerText')
			
	driver_mail25.close()  
	driver25.find_element_by_id("authcode").send_keys(CODE)   
	ui.WebDriverWait(driver25, 20).until(lambda driver25: driver25.find_elements(By.CSS_SELECTOR,"#success_continue_btn"))
	time.sleep(3)
	driver25.find_elements(By.CSS_SELECTOR,"#success_continue_btn")[0].click()              
	ui.WebDriverWait(driver25, 20).until(lambda driver25: driver25.find_elements(By.CSS_SELECTOR,"#iAgree"))
	time.sleep(2)
	driver25.find_elements(By.CSS_SELECTOR,"#iAgree")[0].click()  
	time.sleep(2)
	driver25.find_elements(By.CSS_SELECTOR,"body > div.ReactModalPortal > div > div > div > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix > div > button")[0].click()  
	ui.WebDriverWait(driver25, 20).until(lambda driver25: driver25.find_elements(By.CSS_SELECTOR,"i.visible-phone.fa.fa-gift"))
	time.sleep(2)
	driver25.find_elements(By.CSS_SELECTOR,"i.visible-phone.fa.fa-gift")[0].click()
	try:
		ui.WebDriverWait(driver25, 20).until(lambda driver25: driver25.find_elements(By.CSS_SELECTOR,"button.claimReward"))
		time.sleep(1)
		driver25.find_elements(By.CSS_SELECTOR,"button.claimReward")[0].click()
		ui.WebDriverWait(driver25, 20).until(lambda driver25: driver25.find_elements(By.CSS_SELECTOR,"button.claimRewardDisabled"))
		time.sleep(2)
		driver25.find_elements(By.CSS_SELECTOR,"i.visible-phone.fa.fa-user-plus")[0].click()
		ui.WebDriverWait(driver25, 20).until(lambda driver25: driver25.find_elements(By.CSS_SELECTOR,"#referral_code"))
		time.sleep(2)
		driver25.find_elements(By.CSS_SELECTOR,"#referral_code")[0].send_keys("111111111122")
		time.sleep(3)
		driver25.find_elements(By.CSS_SELECTOR,"#tabs-inner-container > div.widget-container.container-for-affiliate > div > div > div:nth-child(1) > button")[0].click()
		time.sleep(2)
		driver25.find_elements(By.CSS_SELECTOR,"#tabs-inner-container > div.widget-container.container-for-affiliate > div > div > div:nth-child(1) > button")[0].click()
		time.sleep(2)
		driver25.execute_script("arguments[0].scrollIntoView();", driver25.find_elements(By.CSS_SELECTOR,"#tabs-inner-container > div.widget-container.container-for-affiliate > div > div > div.total-money > button")[0])
		time.sleep(1)                       
		driver25.find_elements(By.CSS_SELECTOR,"#tabs-inner-container > div.widget-container.container-for-affiliate > div > div > div.total-money > button")[0].click()
		time.sleep(2)
		driver25.find_elements(By.CSS_SELECTOR,"#tabs-inner-container > div.widget-container.container-for-affiliate > div > div > div.total-money > button")[0].click()
				 
	except:
		print("exception")   
except:
	print("exception") 		
	
#----------------------------------------------------------- CREATE CHROME 6
chrome_options26 = webdriver.ChromeOptions() 
chrome_options26.add_argument("user-agent=firefox")
chrome_options26.add_argument("user-data-dir=C:\\chrome\\Profile-6Work") 
driver26 = webdriver.Chrome(chrome_options=chrome_options26) 
driver26.set_page_load_timeout(120)
driver26.get("http://www.gamdom.com")
result = ui.WebDriverWait(driver26, 40).until(lambda driver26: driver26.find_element_by_id("welcomeDialogText")) 
driver26.find_element_by_id("iAgree").click()
driver26.find_elements(By.CSS_SELECTOR,"a.button.login.icon ")[0].click()
result = ui.WebDriverWait(driver26, 40).until(lambda driver26: driver26.find_element_by_id("steamAccountName")) 
acc = accs.pop()
try:
    driver26.find_element_by_id("steamAccountName").send_keys(acc.split(":")[0])
    driver26.find_element_by_id("steamPassword").send_keys(acc.split(":")[1])
    driver26.find_element_by_id("imageLogin").click()
except:
    print("some exception ")
chrome_options_mail26 = webdriver.ChromeOptions() 
chrome_options_mail26.add_argument("user-agent=firefox")
driver_mail26 = webdriver.Chrome(chrome_options=chrome_options_mail26) 
driver_mail26.delete_all_cookies()
driver_mail26.set_page_load_timeout(120) 
driver_mail26.get("https://temp-mail.org/ru/option/change/")
try:
	first_result = ui.WebDriverWait(driver_mail2, 12).until(lambda driver_mail2: driver_mail26.find_element_by_name("mail"))
	driver_mail26.find_element_by_name("mail").clear()
	driver_mail26.find_element_by_name("mail").send_keys(acc.split(":")[2].split("@")[0])
	Select(driver_mail26.find_element_by_id('domain')).select_by_visible_text("@zep-hyr.com")
	driver_mail26.find_element_by_id("postbut").click()
	driver_mail26.get("https://temp-mail.org/ru")
	ui.WebDriverWait(driver_mail26, 50).until(lambda driver_mail26: driver_mail26.find_element_by_id("mails"))
	time.sleep(2)
	rows = driver_mail26.find_elements(By.CSS_SELECTOR,"a.title-subject")
	for row in rows[::-1]:
		if (row.get_attribute("innerText")=="Your Steam account: Acces"):
			print("-- HAVE STEAM "+row.get_attribute("href"))
			driver_mail26.get(row.get_attribute("href"))
			break
	ui.WebDriverWait(driver_mail26, 50).until(lambda driver_mail26: driver_mail26.find_elements(By.CSS_SELECTOR,"div.mailView"))
	CODE = "NO"
	trs = driver_mail26.find_elements(By.CSS_SELECTOR,"table")[1].find_elements(By.CSS_SELECTOR,"tr")
	for i, tr in enumerate(trs):
		if (tr.get_attribute('innerText').find("Here is the Steam Guard code you need to login to account")!=-1):
			CODE=trs[i+1].get_attribute('innerText')
			
	driver_mail26.close()  
	driver26.find_element_by_id("authcode").send_keys(CODE)   
	ui.WebDriverWait(driver26, 20).until(lambda driver26: driver26.find_elements(By.CSS_SELECTOR,"#success_continue_btn"))
	time.sleep(3)
	driver26.find_elements(By.CSS_SELECTOR,"#success_continue_btn")[0].click()              
	ui.WebDriverWait(driver26, 20).until(lambda driver26: driver26.find_elements(By.CSS_SELECTOR,"#iAgree"))
	time.sleep(2)
	driver26.find_elements(By.CSS_SELECTOR,"#iAgree")[0].click()  
	time.sleep(2)
	driver26.find_elements(By.CSS_SELECTOR,"body > div.ReactModalPortal > div > div > div > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix > div > button")[0].click()  
	ui.WebDriverWait(driver26, 20).until(lambda driver26: driver26.find_elements(By.CSS_SELECTOR,"i.visible-phone.fa.fa-gift"))
	time.sleep(2)
	driver26.find_elements(By.CSS_SELECTOR,"i.visible-phone.fa.fa-gift")[0].click()
	try:
		ui.WebDriverWait(driver26, 20).until(lambda driver26: driver26.find_elements(By.CSS_SELECTOR,"button.claimReward"))
		time.sleep(1)
		driver26.find_elements(By.CSS_SELECTOR,"button.claimReward")[0].click()
		ui.WebDriverWait(driver26, 20).until(lambda driver26: driver26.find_elements(By.CSS_SELECTOR,"button.claimRewardDisabled"))
		time.sleep(2)
		driver26.find_elements(By.CSS_SELECTOR,"i.visible-phone.fa.fa-user-plus")[0].click()
		ui.WebDriverWait(driver26, 20).until(lambda driver26: driver26.find_elements(By.CSS_SELECTOR,"#referral_code"))
		time.sleep(2)
		driver26.find_elements(By.CSS_SELECTOR,"#referral_code")[0].send_keys("111111111122")
		time.sleep(3)
		driver26.find_elements(By.CSS_SELECTOR,"#tabs-inner-container > div.widget-container.container-for-affiliate > div > div > div:nth-child(1) > button")[0].click()
		time.sleep(2)
		driver26.find_elements(By.CSS_SELECTOR,"#tabs-inner-container > div.widget-container.container-for-affiliate > div > div > div:nth-child(1) > button")[0].click()
		time.sleep(2)
		driver26.execute_script("arguments[0].scrollIntoView();", driver26.find_elements(By.CSS_SELECTOR,"#tabs-inner-container > div.widget-container.container-for-affiliate > div > div > div.total-money > button")[0])
		time.sleep(1)                       
		driver26.find_elements(By.CSS_SELECTOR,"#tabs-inner-container > div.widget-container.container-for-affiliate > div > div > div.total-money > button")[0].click()
		time.sleep(2)
		driver26.find_elements(By.CSS_SELECTOR,"#tabs-inner-container > div.widget-container.container-for-affiliate > div > div > div.total-money > button")[0].click()
				 
	except:
		print("exception")  
except:
	print("exception") 
		
#----------------------------------------------------------- CREATE CHROME 7
chrome_options27 = webdriver.ChromeOptions() 
chrome_options27.add_argument("user-agent=firefox")
chrome_options27.add_argument("user-data-dir=C:\\chrome\\Profile-7Work") 
driver27 = webdriver.Chrome(chrome_options=chrome_options27) 
driver27.set_page_load_timeout(120)
driver27.get("http://www.gamdom.com")
result = ui.WebDriverWait(driver27, 40).until(lambda driver27: driver27.find_element_by_id("welcomeDialogText")) 
driver27.find_element_by_id("iAgree").click()
driver27.find_elements(By.CSS_SELECTOR,"a.button.login.icon ")[0].click()
result = ui.WebDriverWait(driver27, 40).until(lambda driver27: driver27.find_element_by_id("steamAccountName")) 
acc = accs.pop()
try:
    driver27.find_element_by_id("steamAccountName").send_keys(acc.split(":")[0])
    driver27.find_element_by_id("steamPassword").send_keys(acc.split(":")[1])
    driver27.find_element_by_id("imageLogin").click()
except:
    print("some exception ")
chrome_options_mail27 = webdriver.ChromeOptions() 
chrome_options_mail27.add_argument("user-agent=firefox")
driver_mail27 = webdriver.Chrome(chrome_options=chrome_options_mail27) 
driver_mail27.delete_all_cookies()
driver_mail27.set_page_load_timeout(120) 
driver_mail27.get("https://temp-mail.org/ru/option/change/")
try:
	first_result = ui.WebDriverWait(driver_mail2, 12).until(lambda driver_mail2: driver_mail27.find_element_by_name("mail"))
	driver_mail27.find_element_by_name("mail").clear()
	driver_mail27.find_element_by_name("mail").send_keys(acc.split(":")[2].split("@")[0])
	Select(driver_mail27.find_element_by_id('domain')).select_by_visible_text("@zep-hyr.com")
	driver_mail27.find_element_by_id("postbut").click()
	driver_mail27.get("https://temp-mail.org/ru")
	ui.WebDriverWait(driver_mail27, 50).until(lambda driver_mail27: driver_mail27.find_element_by_id("mails"))
	time.sleep(2)
	rows = driver_mail27.find_elements(By.CSS_SELECTOR,"a.title-subject")
	for row in rows[::-1]:
		if (row.get_attribute("innerText")=="Your Steam account: Acces"):
			print("-- HAVE STEAM "+row.get_attribute("href"))
			driver_mail27.get(row.get_attribute("href"))
			break
	ui.WebDriverWait(driver_mail27, 50).until(lambda driver_mail27: driver_mail27.find_elements(By.CSS_SELECTOR,"div.mailView"))
	CODE = "NO"
	trs = driver_mail27.find_elements(By.CSS_SELECTOR,"table")[1].find_elements(By.CSS_SELECTOR,"tr")
	for i, tr in enumerate(trs):
		if (tr.get_attribute('innerText').find("Here is the Steam Guard code you need to login to account")!=-1):
			CODE=trs[i+1].get_attribute('innerText')
			
	driver_mail27.close()  
	driver27.find_element_by_id("authcode").send_keys(CODE)   
	ui.WebDriverWait(driver27, 20).until(lambda driver27: driver27.find_elements(By.CSS_SELECTOR,"#success_continue_btn"))
	time.sleep(3)
	driver27.find_elements(By.CSS_SELECTOR,"#success_continue_btn")[0].click()              
	ui.WebDriverWait(driver27, 20).until(lambda driver27: driver27.find_elements(By.CSS_SELECTOR,"#iAgree"))
	time.sleep(2)
	driver27.find_elements(By.CSS_SELECTOR,"#iAgree")[0].click()  
	time.sleep(2)
	driver27.find_elements(By.CSS_SELECTOR,"body > div.ReactModalPortal > div > div > div > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix > div > button")[0].click()  
	ui.WebDriverWait(driver27, 20).until(lambda driver27: driver27.find_elements(By.CSS_SELECTOR,"i.visible-phone.fa.fa-gift"))
	time.sleep(2)
	driver27.find_elements(By.CSS_SELECTOR,"i.visible-phone.fa.fa-gift")[0].click()
	try:
		ui.WebDriverWait(driver27, 20).until(lambda driver27: driver27.find_elements(By.CSS_SELECTOR,"button.claimReward"))
		time.sleep(1)
		driver27.find_elements(By.CSS_SELECTOR,"button.claimReward")[0].click()
		ui.WebDriverWait(driver27, 20).until(lambda driver27: driver27.find_elements(By.CSS_SELECTOR,"button.claimRewardDisabled"))
		time.sleep(2)
		driver27.find_elements(By.CSS_SELECTOR,"i.visible-phone.fa.fa-user-plus")[0].click()
		ui.WebDriverWait(driver27, 20).until(lambda driver27: driver27.find_elements(By.CSS_SELECTOR,"#referral_code"))
		time.sleep(2)
		driver27.find_elements(By.CSS_SELECTOR,"#referral_code")[0].send_keys("111111111122")
		time.sleep(3)
		driver27.find_elements(By.CSS_SELECTOR,"#tabs-inner-container > div.widget-container.container-for-affiliate > div > div > div:nth-child(1) > button")[0].click()
		time.sleep(2)
		driver27.find_elements(By.CSS_SELECTOR,"#tabs-inner-container > div.widget-container.container-for-affiliate > div > div > div:nth-child(1) > button")[0].click()
		time.sleep(2)
		driver27.execute_script("arguments[0].scrollIntoView();", driver27.find_elements(By.CSS_SELECTOR,"#tabs-inner-container > div.widget-container.container-for-affiliate > div > div > div.total-money > button")[0])
		time.sleep(1)                       
		driver27.find_elements(By.CSS_SELECTOR,"#tabs-inner-container > div.widget-container.container-for-affiliate > div > div > div.total-money > button")[0].click()
		time.sleep(2)
		driver27.find_elements(By.CSS_SELECTOR,"#tabs-inner-container > div.widget-container.container-for-affiliate > div > div > div.total-money > button")[0].click()
				 
	except:
		print("exception") 
except:
	print("exception")		

#----------------------------------------------------------- CREATE CHROME 8
chrome_options28 = webdriver.ChromeOptions() 
chrome_options28.add_argument("user-agent=firefox")
chrome_options28.add_argument("user-data-dir=C:\\chrome\\Profile-8Work") 
driver28 = webdriver.Chrome(chrome_options=chrome_options28) 
driver28.set_page_load_timeout(120)
driver28.get("http://www.gamdom.com")
result = ui.WebDriverWait(driver28, 40).until(lambda driver28: driver28.find_element_by_id("welcomeDialogText")) 
driver28.find_element_by_id("iAgree").click()
driver28.find_elements(By.CSS_SELECTOR,"a.button.login.icon ")[0].click()
result = ui.WebDriverWait(driver28, 40).until(lambda driver28: driver28.find_element_by_id("steamAccountName")) 
acc = accs.pop()
try:
    driver28.find_element_by_id("steamAccountName").send_keys(acc.split(":")[0])
    driver28.find_element_by_id("steamPassword").send_keys(acc.split(":")[1])
    driver28.find_element_by_id("imageLogin").click()
except:
    print("some exception ")
chrome_options_mail28 = webdriver.ChromeOptions() 
chrome_options_mail28.add_argument("user-agent=firefox")
driver_mail28 = webdriver.Chrome(chrome_options=chrome_options_mail28) 
driver_mail28.delete_all_cookies()
driver_mail28.set_page_load_timeout(120) 
driver_mail28.get("https://temp-mail.org/ru/option/change/")
try:
	first_result = ui.WebDriverWait(driver_mail2, 12).until(lambda driver_mail2: driver_mail28.find_element_by_name("mail"))
	driver_mail28.find_element_by_name("mail").clear()
	driver_mail28.find_element_by_name("mail").send_keys(acc.split(":")[2].split("@")[0])
	Select(driver_mail28.find_element_by_id('domain')).select_by_visible_text("@zep-hyr.com")
	driver_mail28.find_element_by_id("postbut").click()
	driver_mail28.get("https://temp-mail.org/ru")
	ui.WebDriverWait(driver_mail28, 50).until(lambda driver_mail28: driver_mail28.find_element_by_id("mails"))
	time.sleep(2)
	rows = driver_mail28.find_elements(By.CSS_SELECTOR,"a.title-subject")
	for row in rows[::-1]:
		if (row.get_attribute("innerText")=="Your Steam account: Acces"):
			print("-- HAVE STEAM "+row.get_attribute("href"))
			driver_mail28.get(row.get_attribute("href"))
			break
	ui.WebDriverWait(driver_mail28, 50).until(lambda driver_mail28: driver_mail28.find_elements(By.CSS_SELECTOR,"div.mailView"))
	CODE = "NO"
	trs = driver_mail28.find_elements(By.CSS_SELECTOR,"table")[1].find_elements(By.CSS_SELECTOR,"tr")
	for i, tr in enumerate(trs):
		if (tr.get_attribute('innerText').find("Here is the Steam Guard code you need to login to account")!=-1):
			CODE=trs[i+1].get_attribute('innerText')
			
	driver_mail28.close()  
	driver28.find_element_by_id("authcode").send_keys(CODE)   
	ui.WebDriverWait(driver28, 20).until(lambda driver28: driver28.find_elements(By.CSS_SELECTOR,"#success_continue_btn"))
	time.sleep(3)
	driver28.find_elements(By.CSS_SELECTOR,"#success_continue_btn")[0].click()              
	ui.WebDriverWait(driver28, 20).until(lambda driver28: driver28.find_elements(By.CSS_SELECTOR,"#iAgree"))
	time.sleep(2)
	driver28.find_elements(By.CSS_SELECTOR,"#iAgree")[0].click()  
	time.sleep(2)
	driver28.find_elements(By.CSS_SELECTOR,"body > div.ReactModalPortal > div > div > div > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix > div > button")[0].click()  
	ui.WebDriverWait(driver28, 20).until(lambda driver28: driver28.find_elements(By.CSS_SELECTOR,"i.visible-phone.fa.fa-gift"))
	time.sleep(2)
	driver28.find_elements(By.CSS_SELECTOR,"i.visible-phone.fa.fa-gift")[0].click()
	try:
		ui.WebDriverWait(driver28, 20).until(lambda driver28: driver28.find_elements(By.CSS_SELECTOR,"button.claimReward"))
		time.sleep(1)
		driver28.find_elements(By.CSS_SELECTOR,"button.claimReward")[0].click()
		ui.WebDriverWait(driver28, 20).until(lambda driver28: driver28.find_elements(By.CSS_SELECTOR,"button.claimRewardDisabled"))
		time.sleep(2)
		driver28.find_elements(By.CSS_SELECTOR,"i.visible-phone.fa.fa-user-plus")[0].click()
		ui.WebDriverWait(driver28, 20).until(lambda driver28: driver28.find_elements(By.CSS_SELECTOR,"#referral_code"))
		time.sleep(2)
		driver28.find_elements(By.CSS_SELECTOR,"#referral_code")[0].send_keys("111111111122")
		time.sleep(3)
		driver28.find_elements(By.CSS_SELECTOR,"#tabs-inner-container > div.widget-container.container-for-affiliate > div > div > div:nth-child(1) > button")[0].click()
		time.sleep(2)
		driver28.find_elements(By.CSS_SELECTOR,"#tabs-inner-container > div.widget-container.container-for-affiliate > div > div > div:nth-child(1) > button")[0].click()
		time.sleep(2)
		driver28.execute_script("arguments[0].scrollIntoView();", driver28.find_elements(By.CSS_SELECTOR,"#tabs-inner-container > div.widget-container.container-for-affiliate > div > div > div.total-money > button")[0])
		time.sleep(1)                       
		driver28.find_elements(By.CSS_SELECTOR,"#tabs-inner-container > div.widget-container.container-for-affiliate > div > div > div.total-money > button")[0].click()
		time.sleep(2)
		driver28.find_elements(By.CSS_SELECTOR,"#tabs-inner-container > div.widget-container.container-for-affiliate > div > div > div.total-money > button")[0].click()
				 
	except:
		print("exception")     
except:
	print("exception")
    
    
print("------FINISHED------")

#%%
driver.close()
driver2.close()
driver23.close()
driver24.close()
driver25.close()
driver26.close()
driver27.close()
driver28.close()
shutil.rmtree('C:\\chrome\\Profile-1Work', ignore_errors=True)
shutil.rmtree('C:\\chrome\\Profile-2Work', ignore_errors=True)
shutil.rmtree('C:\\chrome\\Profile-3Work', ignore_errors=True)
shutil.rmtree('C:\\chrome\\Profile-4Work', ignore_errors=True)
shutil.rmtree('C:\\chrome\\Profile-5Work', ignore_errors=True)
shutil.rmtree('C:\\chrome\\Profile-6Work', ignore_errors=True)
shutil.rmtree('C:\\chrome\\Profile-7Work', ignore_errors=True)
shutil.rmtree('C:\\chrome\\Profile-8Work', ignore_errors=True)











