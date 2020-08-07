from selenium import webdriver
#pip install selenium
import time
#download chrome web driver and add it to path
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome()
# I am using chrome for this
driver.get('https://sitetobeloggedin')
#opens the site in a new browser window
#this time mentioned is for the user to see
text_area = driver.find_element_by_id('username')
#finding where to fill the text
#sendig the text to be filled
text_area.send_keys("username")
text_area = driver.find_element_by_id('password')
text_area.send_keys("typepassword")
# click submit button
submit_button = driver.find_elements_by_xpath('//*[@id="app__container"]/div[1]/div/form/div[3]/button')[0]
#chrome inspect and copy the x path of the button to be clicked
submit_button.click()
time.sleep(6)
#waiting time
driver.quit()
#Remember some wewbsites can detect that you are using  a bot so it is better to set some sleep time and login manually
#finally closes it

