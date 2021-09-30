import random

import numpy
'''
random.randint()方法里面的取值区间是前闭后闭区间，
而numpy.random.randint()方法的取值区间是前闭后开区间
'''
result = random.randint(10, 20)
res = numpy.random.randn(5)
res2 = numpy.random.randint(1, 10)
ret = random.random()

print(result)
print(res)

for i in range(1, 10):
    print(random.randint(1, 10), end=' ')
print()
for i in range(1, 10):
    print(numpy.random.randint(1, 10, (2, 4)), end=' ')

print()
print(ret)
'''
numpy.random.randint(low, high=None, size=None, dtype='l')
#这个方法产生离散均匀分布的整数，这些整数大于等于low，小于high。
low : int        #产生随机数的最小值
high : int, optional    #给随机数设置个上限，即产生的随机数必须小于high
size : int or tuple of ints, optional    #整数，生成随机元素的个数或者元组，数组的行和列
dtype : dtype, optional    #期望结果的类型
'''

# 生成0-100的随机数
# 随机小数
res1 = 100*random.random()
# 随机整数
res2=random.choice(range(0,101))
# 随机整数
res3=random.randint(1,100)
print(res1)
print(res2)
print(res3)