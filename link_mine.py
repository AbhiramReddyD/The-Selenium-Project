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
driver.get('https://www.linkedin.com/uas/login')
#opens the site in a new browser window
#this time mentioned is for the user to see
text_area = driver.find_element_by_id('username')
#finding where to fill the text
#sendig the text to be filled
text_area.send_keys("user@gmail.com")
text_area = driver.find_element_by_id('password')
text_area.send_keys("pswd")
# click submit button
submit_button = driver.find_elements_by_xpath('//*[@id="app__container"]/main/div/form/div[3]/button')[0]
submit_button.click()
s=[]
s=["Amitab Bachan","Samantha","Mark Zuckerberg"]
print(s[0])
l=(len(s))

def search(m):
    driver.get("https://www.linkedin.com/feed/")
    search=driver.find_element_by_xpath("//*[@id=\"ember35\"]/input")
    search.send_keys(m,"\n")
    time.sleep(5)
    print("Seraching",m)
    res=[]
    for a in driver.find_elements_by_xpath('.//a'):
        res.append(a.get_attribute("href"))
    n=""
    n=m.lower()
    n=n.replace(" ","-")
    print(n)
    #these if statements are for getting exact links to the resultant profiles
    for i in range (len(res)):
        if n in res[i]:
            print(res[i])

for i in range(len(s)):
    z=s[i]
    search(z)
#finally closes it

#this is most siple way to start and test the use of selenium
