from aip import AipOcr
import requests
import os
APP_ID = '18299361'
API_KEY = '9hEv8TpZgVncF2URmE2qkASg'
SECRET_KEY = '3CcfWFZ8HhToGT94lFUcwZr5TlewG02s'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def ocr_image():
    with open('./code.png', 'rb') as fp:
        code_image = fp.read()
        result = client.webImage(code_image)
        print(result)
        delete_old_code_image
        return result

def down_load_image(url='https://login.sina.com.cn/cgi/pin.php?r=81705044&s=0&p=gz-57605e78f793a8bcef37f2f49e663fc8698b'):
    ir = requests.get(url)
    print(ir)
    if ir.status_code == 200:
        delete_old_code_image()
        with open('code.png', 'wb') as f:
            f.write(ir.content)
def delete_old_code_image():
    image_code_path='./code.jpg'
    if os.path.exists(image_code_path):
        os.remove(image_code_path)
        print('romove file:%s success' % image_code_path)
    else:
        print ('no such file:%s' % image_code_path)
# down_load_image()
# ocr_image()