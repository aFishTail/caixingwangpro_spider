from time import sleep

from ocr import ocr_image
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def check_ocr(verification_result):
    if verification_result['words_result_num'] == 0:
        return False
    else:
        return True

def verify(driver):
    ele_verification_code = driver.find_element_by_xpath(
        '//*[@id="outer"]/div/div[2]/form/div/div[1]/div[1]/p[3]/span/img')
    ele_verification_code.screenshot('./code.png')
    sleep(1)
    re_test_button = driver.find_element_by_xpath('//*[@id="outer"]/div/div[2]/form/div/div[1]/div[1]/p[3]/a')
    verification_result = ocr_image()
    while (not check_ocr(verification_result)):
        print('验证吗ocr识别失败')
        re_test_button.click()
        sleep(1)
        ele_verification_code.screenshot('./code.png')
        sleep(1)
        verification_result = ocr_image()
    verification_code = verification_result['words_result'][0]['words']
    login(driver, verification_code)

def login(driver, verification_code):
        ele_verification_input = driver.find_element_by_xpath(
            '//*[@id="outer"]/div/div[2]/form/div/div[1]/div[1]/p[3]/input')
        ele_verification_input.send_keys(verification_code)
        login_button = driver.find_element_by_xpath('//*[@id="outer"]/div/div[2]/form/div/div[2]/div/p/a[1]')
        login_button.click()
        sleep(1)

        try:
            driver.find_element_by_xpath('//*[@id="outer"]/div/div[2]/form/div/div[1]/div[2]').is_displayed()
        except:
            print('验证码登录失败，重新识别进行登录')
            verify(driver)
        else:
            sleep(1)
            print('登录成功')




