import re

s1 = 'adkkdk'

# 判断s1字符串是否负责都为小写的正则
an = re.search('^[a-z]+$', s1)
if an:
    print(True)
else:
    print(False)

str = "linchang"
res1 = re.search('^[0-9a-z\\-_.]{1,}$', str)
if not res1:
    print('1.1输入必须为小写字母数字或_-.')

res1 = re.search('^[0-9a-z\\-_.]+$', str)
if not res1:
    print('1.2输入必须为小写字母数字或_-.')

res1 = re.search('[0-9a-z\\-_.]+$', str)
if res1:
    print('1.3输入必须为小写字母数字或_-.此处错误！')

res2 = re.search('^[0-9a-zA-Z]+$', str)
if not res2:
    print('2.1输入必须为字母、数字')

res2 = re.search('[0-9a-zA-Z]+$', str)
if res2:
    print('2.2输入必须为字母、数字')

res2 = re.search('^[0-9a-zA-Z-\\u4e00-\\u9fa5]+$', str)
if not res2:
    print('3输入必须为字母、数字或中文')

print('-----------------不好用start--------------------')
uid = 'linchang'
surname = 'yijiu汉'
name = 'chang'
res = re.search("[0-9a-z\\-_.]+$", uid)
print(res)
if not res:
    print('输入必须为小写字母数字或_-.')

res = re.search("[0-9a-zA-Z-\\u4e00-\\u9fa5]+$", surname)
print(res)
if not res:
    print('输入必须为字母、数字或中文')

res = re.search("[0-9a-zA-Z-\\u4e00-\\u9fa5]+$", name)
print(res)
if not res:
    print('输入必须为字母、数字或中文')

print('-----------------不好用end--------------------')

password = 'yijiu@@!！汉'
res = re.search('[\\u4e00-\\u9fa5]+$', password)
print(res)
if res:
    print('输入不能包含中文')

password = 'qw)）'
res = re.search('[\\u0391-\\uffe5]', password)
print(res)
if res:
    print('输入不能包含中文')

pattern = r'^1(3([0-35-9]\d|4[1-8])|4[14-9]\d|5([0125689]\d|7[1-79])|66\d|7[2-35-8]\d|8\d{2}|9[13589]\d)' \
          r'\d{7}$'
phone = '1892095576a'
res = re.search(pattern, phone)
print(res)
if not res:
    print('输入非手机号')

pattern = r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$'
mail = '1892095576@a.com'
res = re.search(pattern, mail)
print(res)
if not res:
    print('输入非邮箱')
