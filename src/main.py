from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

u = "username"
p = "password"
s = "target username"
spam_message = "message"

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://www.instagram.com")

driver.implicitly_wait(20)
userName = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")
userName.send_keys(u)
userName.send_keys(Keys.RETURN)
password.send_keys(p)
password.send_keys(Keys.RETURN)
kaydetme = driver.find_element_by_class_name("yWX7d").click()
time.sleep(2)
driver.get("https://www.instagram.com/direct/inbox/")
time.sleep(2)
skipButton = driver.find_element_by_class_name("HoLwm").click()
time.sleep(2)
newMessage = driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button").click()
time.sleep(2)
search = driver.find_element_by_name("queryBox")
search.send_keys(s)
search.send_keys(Keys.RETURN)
time.sleep(2)
userDiv = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div[2]/div[1]").click()
time.sleep(2)
nextButton = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/div/button/div").click()
time.sleep(2)
messageText = driver.find_element_by_xpath(
    "//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
messageText.send_keys(spam_message)
messageText.send_keys(Keys.RETURN)
time.sleep(2)
i = 0
while i < 200:
    messageText.send_keys(spam_message)
    messageText.send_keys(Keys.RETURN)
    i += 1


#time.sleep(5)
#driver.quit()