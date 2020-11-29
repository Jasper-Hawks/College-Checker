'''
Created on Nov 15, 2020
Completed on Nov 28, 2020
@author: Jasper Hawks
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox() # Opens the windows in firefox
user = ""
password = ""

#By default this script will not work since I
#do not want to give away my password

Colleges = ["https://admission.wm.edu/apply/status","https://georgemasonuniversity.force.com/portal/TargetX_Base__Portal#/","https://admissions.vcu.edu/apply/status","https://odu.force.com/portal/TargetX_Base__Portal#/","https://admit.vt.edu/portal/status","https://mymadison.ps.jmu.edu/psp/pprd/JMU/CUST/h/?tab=JPS_APPLICANT"]

'''
Contains links to colleges seperated by a comma.

You can replace the five links with other links 
though logging in will usually fail since HTML
elements are not universal. Some elements such 
as IDs may not work with Selenium, so the XPath
is usually your next best bet.

'''

# William and Mary
driver.get(Colleges[0]) #Sends us to the link specified in the Colleges array
UserField = driver.find_element_by_id("email") #Scans the page  to find the given element
UserField.send_keys(user) #Prints the user variable into the field
PassField = driver.find_element_by_id("password") #Finds the HTML element
PassField.send_keys(password) #Prints the password variable
Login = driver.find_element_by_xpath("/html/body/div[2]/div/main/div/div[2]/form/table/tbody/tr/td[1]/div/button") #Finds the login button
Login.click() #Clicks the login button
        
driver.execute_script("window.open('about:blank', 'tab2');") #Executes script to open another tab named tab2
driver.switch_to.window("tab2") #Then switches to that tab 

# This is then repeated 5 times for the five universities.

# George Mason

driver.get(Colleges[1])
UserField = driver.find_element_by_id("j_id0:j_id1:siteLogin:loginComponent:loginForm:username")
UserField.send_keys(user)
PassField = driver.find_element_by_id("j_id0:j_id1:siteLogin:loginComponent:loginForm:password")
PassField.send_keys(password)
Login = driver.find_element_by_xpath("//*[@id=\"j_id0:j_id1:siteLogin:loginComponent:loginForm:submitForm\"]")
Login.click()


driver.execute_script("window.open('about:blank','tab3' );")
driver.switch_to.window("tab3")  

# VCU

driver.get(Colleges[2])
UserField = driver.find_element_by_id("email")
UserField.send_keys(user)
PassField = driver.find_element_by_id("password")
PassField.send_keys(password)
Login = driver.find_element_by_xpath("/html/body/div[2]/div/div[6]/div[1]/div/div/div/div/div/div/div[2]/form/table/tbody/tr/td[1]/div/button")
Login.click()

driver.execute_script("window.open('about:blank', 'tab4');")
driver.switch_to.window("tab4")  

# ODU

driver.get(Colleges[3])
UserField = driver.find_element_by_id("j_id0:j_id1:siteLogin:loginComponent:loginForm:username")
UserField.send_keys(user)
PassField = driver.find_element_by_id("j_id0:j_id1:siteLogin:loginComponent:loginForm:password")
PassField.send_keys(password)
Login = driver.find_element_by_xpath("//*[@id=\"submitForm\"]")
Login.click()

driver.execute_script("window.open('about:blank', 'tab5');")
driver.switch_to.window("tab5")  

#Virginia Tech

driver.get(Colleges[4])
UserField = driver.find_element_by_id("username")
UserField.send_keys(user)
PassField = driver.find_element_by_id("password")
PassField.send_keys(password)
Login = driver.find_element_by_xpath("/html/body/main/div/form/fieldset/div[3]/button")
Login.click()

driver.execute_script("window.open('about:blank', 'tab6');")
driver.switch_to.window("tab6")  

#JMU

driver.get(Colleges[5])
UserField = driver.find_element_by_xpath("//*[@id=\"userid\"]")
UserField.send_keys(user)
PassField = driver.find_element_by_id("password")
PassField.send_keys(password)
Login = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/form/ul[1]/li[3]/input")
Login.click()

print("Done") #Then writes done


