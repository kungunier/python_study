import requests
import time
from PIL import Image
import io
import pytesseract

captcha_url = 'https://bstest.motie.cn:4433/users/captcha?' + str(round(time.time() * 1000))

response = requests.get(captcha_url)
img = Image.open(io.BytesIO(response.content))
img.save('/Users/liuhailong/VscodeProjects/pyCode/python_study/File/captcha.jpg')

def deal_captcha_image(image_path):
    img = Image.open(image_path)
    # img.show()
    img = img.convert('L')

    threshold = 200
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    
    img = img.point(table,'1')
    img.show()

    res = pytesseract.image_to_string(img)
    return res

res = deal_captcha_image('File/captcha.jpg')
print(res)