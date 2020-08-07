from selenium import webdriver
#pip install selenium
import time
import sqlite3 as sq
#download chrome web driver and add it to path
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome()
# I am using chrome for this
driver.get('https://www.linkedin.com/uas/login?session_redirect=%2Fvoyager%2FloginRedirect%2Ehtml&fromSignIn=true&trk=uno-reg-join-sign-in')
#opens the site in a new browser window
#this time mentioned is for the user to see
text_area = driver.find_element_by_id('username')
#finding where to fill the text
#sendig the text to be filled
text_area.send_keys("Your_Email")

text_area = driver.find_element_by_id('password')

text_area.send_keys("yoiurpassword")

# click submit button
submit_button = driver.find_elements_by_xpath('//*[@id="app__container"]/main/div/form/div[3]/button')[0]
time.sleep(11)


driver.quit()

#finally closes it

#this is most siple way to start and test the use of selenium
