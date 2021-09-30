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
