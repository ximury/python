import PySimpleGUI as sg
import pytesseract
import tesserocr
from PIL import Image
from numpy.core.defchararray import translate

import time


def image2word(path, lang):
    try:
        image = Image.open(path)
        words = tesserocr.image_to_text(image, lang=lang)
        return words
    except (OSError, NameError):
        return 'Error!'


path = './csdn.jpeg'
print(image2word(path, 'eng'))
path = './ko.png'
print(image2word(path, 'kor'))

# event, values = sg.Window('选择转文字照片').Layout([
#     [sg.Text('上传照片')],
#     [sg.Input(), sg.FileBrowse('选择文件')],
#     [sg.Radio('开启翻译', 'flag'), sg.Radio('中/英', "choose")],
#     [sg.OK('确认'), sg.Cancel('取消')]
# ]).Read()
#
# if event == '取消':
#     exit('no image file selected!')
# print(values)
#
# image2word(values[0])
# pass
# img_info = Image.open(values[0])
# print(img_info)
# text = pytesseract.image_to_string(Image.open(values[0]), lang='chi_sim')
#
# print(text)
#
# text = str(text).replace('\n', '')
#
# print(text)
# if values[1]:
#     if values[2]:
#         res = translate(text, 'en', 'zh')
#     else:
#         res = translate(text, 'zh', 'en')
#     text = ''
#     for ans in res['trans_result']:
#         text += ans['dst'] + '\n'
