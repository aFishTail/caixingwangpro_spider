from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://baidu.com")
try:
    element = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="kw8"]'))
    )
except:
    print('进入异常')
else:
    print('进入else')
finally:
    print('进入finally')
    driver.quit()