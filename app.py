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

# login_button = driver.find_element_by_xpath('//*[@id="showLoginId"]/li[2]/a')
# login_button.click()
# sleep(1)
#
# weibo_button = driver.find_element_by_xpath('//*[@id="phone"]/a[2]/li/p')
# weibo_button.click()
# sleep(1)
#
# ele_username = driver.find_element_by_xpath('//*[@id="userId"]')
# ele_username.send_keys(username)
# sleep(1)
#
# ele_password = driver.find_element_by_xpath('//*[@id="passwd"]')
# ele_password.send_keys(password)
# sleep(1)
#
# verify(driver)
_cookie="originReferrer=google; GUID=1540809956; CX_FROM=null; T_GUID=1579224674917; point=1579276799000; _gid=GA1.2.1770687039.1579224675; _ga=GA1.2.1509475603.1579224675; gr_user_id=b33beed6-42c4-405e-ae7e-f7dcc416000c; grwng_uid=06d94641-14e7-42d2-8109-f42ce9cac5eb; iwt_uuid=2b906878-807c-460d-9c16-b26a441ab57d; CAIXIN_UUID=4525ff15117e4adf8e62d637633d5cd3; SA_AUTH_TYPE=%E8%B4%A2%E6%96%B0%E7%BD%91; myStast=2020-1-17; trc_cookie_storage=taboola%2520global%253Auser-id%3D046799dc-21c3-4dcd-8ea5-4a564c41e7cb-tuct3947c19; 872f3eaac31f373e_gr_last_sent_cs1=7006099; GID30=1147525972; 872f3eaac31f373e_gr_session_id=b4fda73d-776a-48d5-a419-85d33df45d42; 872f3eaac31f373e_gr_last_sent_sid_with_cs1=b4fda73d-776a-48d5-a419-85d33df45d42; 872f3eaac31f373e_gr_session_id_b4fda73d-776a-48d5-a419-85d33df45d42=true; SA_USER_USER_NAME=; SA_USER_auth=a2ec%2BvySK79Jd8jmk1qBWYEomM8Xh%2F%2B3slI3tdphBhMT8Y9q7rDu1d86RXhU%2BHkhvYL7jzeqNwDVFstTYPE%2FJ7cLKYxtNN4aDAdsRan9rGR%2Bk67zZY%2FnGE9v2wqiBDr%2Bww; UID=7006099; SA_USER_UID=7006099; SA_USER_NICK_NAME=%E5%B8%82%E5%9C%BA%E5%BE%AA%E7%8E%AF%E7%BB%8F%E6%B5%8E; SA_USER_UNIT=1; SA_USER_DEVICE_TYPE=5; USER_LOGIN_CODE=028C0378CDE416EF67C6DB5AB5064398; backUrl=http%3A//database.caixin.com/2020-01-17/101505242.html; ENTITY_ID=101505242; ENTITY_COUNT=0; lastTime=1579250952032; firstTime=1579250952032; 872f3eaac31f373e_gr_cs1=7006099"
cookies = dict([l.split("=", 1) for l in _cookie.split("; ")])
print(cookies)
driver.add_cookie(cookies)
# sleep(3)
# driver.refresh()
# sleep(3)
# print(driver.page_source)


# 关闭浏览器
# driver.close()



def screenshot_code_image(img):
    left = img.location['x']
    top = img.location['y']

    right = img.location['x'] + img.size['width']
    bottom = img.location['y'] + img.size['height']

    driver.get_screenshot_as_file("./screenshot_img.jpg")