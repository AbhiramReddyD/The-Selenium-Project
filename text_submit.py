from selenium import webdriver
import time
 
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome()
driver.get('http:techknowspace.wordpress.com')
 # type text
text_area = driver.find_element_by_id('subscribe-field')
#finding where to fill the text
#sendig the text to be filled
text_area.send_keys("user@gmail.com")
# click submit button
submit_button = driver.find_elements_by_xpath('//*[@id="subscribe-blog"]/p[4]/input[7]')[0]
submit_button.click()
