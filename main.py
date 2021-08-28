from pip._vendor import requests
import urllib
import PIL
import os
from PIL import Image
from io import BytesIO
import time
headers = {
    'User-Agent':'Dalvik/2.1.0(Linux;U;Android8.1.0;FQTODO Build/RKQ1.200000.123)',
    'Host':'poster.fqtodo.cn',
    'Connection':'Keep-Alive',
    'Accept-Encoding':'gzip'
    }
i = 1
while(i < 2000):
    print("Try download pic " + str(i))
    try:
        r = requests.get('http://poster.fqtodo.cn/test' + str(i) + '.png', headers=headers)
        image = Image.open(BytesIO(r.content))
    except PIL.UnidentifiedImageError:
        print("Try download pic " + str(i) + " failed.")
        time.sleep(0.5)
        i += 1
    else:
        print("Try download pic " + str(i) + " succeed")
        image.save('E:/tomatodo/' + str(i) + '.png')
        time.sleep(0.5)
        i += 1
