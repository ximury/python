from functools import partial


def func(a, b):
    return a + b


# 正常使用
result = func(1, 2)

# 使用偏函数导入一个参数，返回一个新函数
# 相当于把原函数中的第一个参数a固定一个值为1，新函数只需要传入一个参数b即可
new_func = partial(func, 1)
result2 = new_func(2)

print(result, result2)
