'''
避免字符串被转义，使用r，比如 \t 字符串
adfdfasd\tfdsadf\t
'''
str = "adfdfasd\tfdsadf\t"
print(str)

str = r"adfdfasd\tfdsadf\t"
print(str)

str = 'sji%qj_jiw_djr%uk'
str = str.replace('_', '\_').replace('%', '\%')
print(str)

print('--------------')

bol = True
print(bol.__str__())

