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
while(i < 3000):
    print("Downloading picture " + str(i))
    try:
        r = requests.get('http://poster.fqtodo.cn/test' + str(i) + '.jpg', headers=headers)
        image = Image.open(BytesIO(r.content))
    except PIL.UnidentifiedImageError:
        try:
            r = requests.get('http://poster.fqtodo.cn/test' + str(i) + '.JPG', headers=headers)
            image = Image.open(BytesIO(r.content))
        except PIL.UnidentifiedImageError:
            try:
                r = requests.get('http://poster.fqtodo.cn/test' + str(i) + '.png', headers=headers)
                image = Image.open(BytesIO(r.content))
            except PIL.UnidentifiedImageError:
                print("Download picture " + str(i) + " failed.")
                time.sleep(0.3)
                i += 1
            else:
                print("Download picture " + str(i) + " succeed")
                image.save('E:/tomatodo/' + str(i) + '.png')
                time.sleep(0.3)
                i += 1
        else:
            print("Download picture " + str(i) + " succeed")
            image.save('E:/tomatodo/' + str(i) + '.JPG')
            time.sleep(0.3)
            i += 1
    else:
        print("Download picture " + str(i) + " succeed")
        image.save('E:/tomatodo/' + str(i) + '.jpg')
        time.sleep(0.3)
        i += 1
i = 1
while(i < 3000):
    print("Downloading picture " + str(i))
    try:
        r = requests.get('http://poster.fqtodo.cn/ab' + str(i) + '.jpg', headers=headers)
        image = Image.open(BytesIO(r.content))
    except PIL.UnidentifiedImageError:
        try:
            r = requests.get('http://poster.fqtodo.cn/ab' + str(i) + '.JPG', headers=headers)
            image = Image.open(BytesIO(r.content))
        except PIL.UnidentifiedImageError:
            try:
                r = requests.get('http://poster.fqtodo.cn/ab' + str(i) + '.png', headers=headers)
                image = Image.open(BytesIO(r.content))
            except PIL.UnidentifiedImageError:
                print("Download picture " + str(i) + " failed.")
                time.sleep(0.3)
                i += 1
            else:
                print("Download picture " + str(i) + " succeed")
                image.save('E:/tomatodo/' + str(i) + '.png')
                time.sleep(0.3)
                i += 1
        else:
            print("Download picture " + str(i) + " succeed")
            image.save('E:/tomatodo/' + str(i) + '.JPG')
            time.sleep(0.3)
            i += 1
    else:
        print("Download picture " + str(i) + " succeed")
        image.save('E:/tomatodo/' + str(i) + '.jpg')
        time.sleep(0.3)
        i += 1