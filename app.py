from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from config import username, password


# 创建Chrome驱动实例
from handle_login import verify
from ocr import ocr_image

driver = webdriver.Chrome()

# 启动浏览器并且导航到指定URL
driver.get("http://database.caixin.com/news/")
sleep(1)

login_button = driver.find_element_by_xpath('//*[@id="showLoginId"]/li[2]/a')
login_button.click()
sleep(1)

weibo_button = driver.find_element_by_xpath('//*[@id="phone"]/a[2]/li/p')
weibo_button.click()
sleep(1)

ele_username = driver.find_element_by_xpath('//*[@id="userId"]')
ele_username.send_keys(username)
sleep(1)

ele_password = driver.find_element_by_xpath('//*[@id="passwd"]')
ele_password.send_keys(password)
sleep(1)

verify(driver)




# 关闭浏览器
# driver.close()



def screenshot_code_image(img):
    left = img.location['x']
    top = img.location['y']

    right = img.location['x'] + img.size['width']
    bottom = img.location['y'] + img.size['height']

    driver.get_screenshot_as_file("./screenshot_img.jpg")