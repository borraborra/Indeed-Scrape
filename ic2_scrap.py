from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv

driver = webdriver.Chrome(r"C:\Users\borra\Desktop\ChromeDriver\chromedriver")

driver.get('https://www.indeed.com/hireV2')
sleep(3)

link_jobs = driver.find_element_by_link_text('Find candidates')

link_jobs.click()
sleep(3)

sign_in = driver.find_element_by_link_text('Sign in')

sign_in.click()
sleep(3)

email_login = driver.find_element_by_name('__email')

email_login.send_keys('username') #input username 
sleep(1)
password_login = driver.find_element_by_name('__password')

password_login.send_keys('password') #input password
sleep(2)

sign_in2 = driver.find_element_by_xpath('//*[@id="login-submit-button"]')
sleep(3)

sign_in2.click()
sleep(3)

search_query = driver.find_element_by_name('q')

search_query.send_keys('Software engineer') #input job title
sleep(2)

location_query = driver.find_element_by_name('l')

location_query.send_keys('Pittsburgh, PA') #input city
sleep(2)

search_resumes = driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div[1]/div/div[2]/div/form/div[2]/div[1]/button')
sleep(3)

search_resumes.click()

jp1 = driver.find_elements_by_xpath('//*[@id="content"]/div/div/div/div[2]/div[1]/div[2]/div[2]/div[3]')

for value in jp1:
    candidate = (value.text)

with open('Indeed_Results1.csv', 'w', newline='') as csvfile: #export results to csv

    fieldnames = ['Indeed Results'] #column names

    thewriter =  csv.DictWriter(csvfile, fieldnames=fieldnames)

    thewriter.writeheader()

    thewriter.writerow({'Indeed Results':candidate})
