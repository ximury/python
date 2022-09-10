import ast
import json

str = "[{'ipSectionStart': '192.168.17.230', 'ipSectionEnd': '192.168.17.24'}," \
      "{'ipSectionStart': '192.168.17.230', 'ipSectionEnd': '192.168.17.24'}]"
# str = str[1:-1]
print(str)
_tuple = ast.literal_eval(str)
print(_tuple, type(_tuple))
li = list(_tuple)
print(li, type(li))
print(li[0], type(li[0]))

print('-----------------------')

str = "[{'ipSectionStart': '192.168.19.199', 'ipSectionEnd': '192.168.19.222'}]"
str = str[1:-1]
print(str)
_tuple = ast.literal_eval(str)
print(_tuple, type(_tuple))
li = list(_tuple)
print(li, type(li))
print(li[0], type(li[0]))

# print('-----------------------')
# str = "[{'ipSectionStart': '192.168.19.199', 'ipSectionEnd': '192.168.19.222'}]"
# li = list(ast.literal_eval(str[1:-1]))
# print(li)


print('-----------------------')

str = "[{'ipSectionStart': '192.168.19.199', 'ipSectionEnd': '192.168.19.222'}]"
print(str)
_tuple = ast.literal_eval(str)
print(_tuple, type(_tuple))
li = list(_tuple)
print(li, type(li))
print(li[0], type(li[0]))

print("==========================")

str = "[1, 2, 3]"
li = ast.literal_eval(str)
print(li, type(li))
print("res: {}".format(li))
