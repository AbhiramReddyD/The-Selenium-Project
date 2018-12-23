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
driver.get('https://www.linkedin.com/uas/login?session_redirect=%2Fvoyager%2FloginRedirect%2Ehtml&fromSignIn=true&trk=uno-reg-join-sign-in')
#opens the site in a new browser window
#this time mentioned is for the user to see
text_area = driver.find_element_by_id('username')
#finding where to fill the text
#sendig the text to be filled
text_area.send_keys("your useranme")

text_area = driver.find_element_by_id('password')

text_area.send_keys("password_here")

# click submit button
submit_button = driver.find_elements_by_xpath('//*[@id="app__container"]/div[1]/div/form/div[3]/button')[0]
time.sleep(1)
submit_button.click()

time.sleep(1)
driver.get("https://www.linkedin.com/search/results/all/?keywords=amitab%20bachan&origin=GLOBAL_SEARCH_HEADER")
#this page opens results for Amitab Bachan profile search on linked in
str=[]

for a in driver.find_elements_by_xpath('.//a'):
    if a.get_attribute("data-control-name")==("search_srp_result"):
        if a.get_attribute("class")==("search-result__result-link search-result__result-link--visited ember-view"):
            str.append(a.get_attribute("href"))
#these if statements are for getting exact links to the resultant profiles

print("Links are:")
x=len(str)
m=0
for m in range(len(str)):
    print(str[m])


time.sleep(10)
driver.quit()

#finally closes it

