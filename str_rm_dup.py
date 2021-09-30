"""
去重并从小到大排序输出
"""
str = "ajldjlajfdljfddd"

str = set(str)
print(str)

str = list(str)

print(str)

str.sort()
print(str)

str.sort(reverse=True)
print(str)

print('--------------------')
str1 = '192.168.17.230'
str2 = '192.168.17.24'
print(str1 > str2)
