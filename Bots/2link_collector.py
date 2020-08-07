from selenium import webdriver
 
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome()
 
driver.get('https://linkedin.com/')
#opens the site
#gather all the links in a site
for a in driver.find_elements_by_xpath('.//a'):
    print(a.get_attribute('href'))
#print all of them
