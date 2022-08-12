from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# thư viện thay cho input
import getpass
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://vietstock.vn/")
pages = driver.find_elements("xpath", "//div[@class='owl-stage']//div[@class='single_post_text']")

l = driver.find_element(By.PARTIAL_LINK_TEXT, "Quỹ đầu tư tiếp tục giao dịch trầm lắng")
driver.execute_script("arguments[0].click();", l)

# WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Quỹ đầu tư tiếp tục giao dịch trầm lắng"))).click()

print('Page navigated after click: ' + driver.title)
time.sleep(2)

y = driver.find_element(By.XPATH, "//p[contains(@class, 'pHead')]")
print(y.text)
print(f"---{y.get_attribute('class')}---")

driver.quit()