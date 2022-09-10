#!/usr/bin/envpython
# -*-coding:UTF-8-*-
import random

# 生成随机6位随机数含字母
code = []
# range(6):0,1,2,3,4,5
for i in range(6):
    # random.randint(0, 5):0,1,2,3,4,5
    if i == random.randint(0, 5):
        code.append(str(random.randint(0, 5)))
    else:
        code.append(chr(random.randint(65, 90)))
print(''.join(code))  # 转换成字符串

print("888888888888888888888888")

for i in range(1, 20):
    print(i)
    n2 = '%05d' % i
    print(n2, type(n2))

print("------------------------")

code = []
for i in range(30):
    # random.randint(0, 5):0,1,2,3,4,5
    if i == random.randint(0, 5):
        code.append(str(random.randint(0, 5)))
    else:
        code.append(chr(random.randint(65, 90)))
    if (i + 1) % 6 == 0:
        code.append("-")
code.pop()
print(''.join(code))  # 转换成字符串
