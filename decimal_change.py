import urllib
from urllib.parse import urlencode, unquote

a = 10
hex_number = hex(a)
print(hex_number)

a = '1qazXsw'
by = bytes(a, 'UTF-8')  # 先将输入的字符串转化成字节码
hex_string = by.hex()
print(hex_string)

a = '!@'
hex_string = ""
for i in range(len(a)):
    hex_string += hex(ord(a[i]))[2:] + "-"
print(hex_string)
print("----------------------------")

base_url = 'base_url = "https://test.cn/'
a = {'name': '123asd!@'}
after = urlencode(a)
print(after, type(after))
before = unquote(after)
print(before, type(before))
res = base_url + urlencode(a)
print(res)

