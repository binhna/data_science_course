from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path='/Users/binhna/projects/resource/chromedriver')
username = input()
password = input()
driver.get("https://trade.vndirect.com.vn/chung-khoan/danh-muc")
user_name = driver.find_element("xpath", "\\div[@class='form-field']/input[@name='username']")
user_name.send_keys(username)
pass_word = driver.find_element("xpath", "\\div[@class='form-field']/input[@name='password']")
pass_word.send_keys(password)