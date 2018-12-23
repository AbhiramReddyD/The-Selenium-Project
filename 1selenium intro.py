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
driver.get('https:techknowspace.wordpress.com')
#opens the site in a new browser window 
#this time mentioned is for the user to see
time.sleep(50)
#finally closes it
driver.quit()
#this is most siple way to start and test the use of selenium
