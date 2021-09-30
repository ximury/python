# zip() 函数用于将可迭代的对象作为参数，
# 将对象中对应的元素打包成一个个元组，
# 然后返回由这些元组组成的列表
a = [1, 2]
b = [3, 4]
res = [i for i in zip(a, b, a)]
print(res)

a = (1, 2)
b = (3, 4, 5)
res = [i for i in zip(a, b)]
print(res)
for (item1, item2) in res:
    print(item1, item2)


a = (1, 2, 3)
b = (4, 5)
res = [i for i in zip(a, b)]
print(res)

a = "abc"
b = "xy"
res = [i for i in zip(a, b)]
print(res)
