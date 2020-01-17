from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from config import username, password

def check_ocr():
    while verification_result['words_result_num'] == 0:
        print('识别失败,刷新验证码')
        re_test_button.click()
        sleep(1)
        ele_verification_code.screenshot('./code.png')
        sleep(1)
        verification_result = ocr_image()
    if verification_result['words_result_num'] > 0:
        verification_code = verification_result['words_result'][0]['words']
        print('识别了验证码', verification_code)
        ele_verification_input = driver.find_element_by_xpath(
            '//*[@id="outer"]/div/div[2]/form/div/div[1]/div[1]/p[3]/input')
        ele_verification_input.send_keys(verification_code)
        login_button.click()
        sleep(1)

# 创建Chrome驱动实例
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

ele_verification_code = driver.find_element_by_xpath('//*[@id="outer"]/div/div[2]/form/div/div[1]/div[1]/p[3]/span/img')
ele_verification_code.screenshot('./code.png')
sleep(1)

re_test_button = driver.find_element_by_xpath('//*[@id="outer"]/div/div[2]/form/div/div[1]/div[1]/p[3]/a')

login_button = driver.find_element_by_xpath('//*[@id="outer"]/div/div[2]/form/div/div[2]/div/p/a[1]')

ele_error_tip = driver.find_element_by_xpath('//*[@id="outer"]/div/div[2]/form/div/div[1]/div[2]')

verification_result = ocr_image()

check_ocr()

if (len(ele_error_tip)>0):
    print('验证输入错误，重新验证')
    check_ocr()
else:
    login_button.click()
# 关闭浏览器
# driver.close()



def screenshot_code_image(img):
    left = img.location['x']
    top = img.location['y']

    right = img.location['x'] + img.size['width']
    bottom = img.location['y'] + img.size['height']

    driver.get_screenshot_as_file("./screenshot_img.jpg")