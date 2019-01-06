from selenium import webdriver
import time
 
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"
#unlike just loading the page this dosen't reload images
prefs = {'profile.managed_default_content_settings.images':2, 'disk-cache-size': 4096}
#using disk cache
#faster loading of pages
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome()
for i in range(50):
    print(i)
    driver.get('https://techknowspace.wordpress.com/2019/01/06/best-mobile-phones-of-2018/')
time.sleep(5)
driver.quit()
