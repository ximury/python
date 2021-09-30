# 不可变数据类型：
# 数值型、字符串型string、布尔型、和元组tuple
# 可变数据类型：
# 列表list和字典dict
"""
不允许变量的值发生变化，
如果改变了变量的值，相当于是新建了一个对象，
而对于相同的值的对象，在内存中则只有一个对象（一个地址）
"""

a = 3
b = 3
print(id(a), id(b))

c = True
d = True
print(id(c), id(d))

# 不同对象，不一样的内存地址
m = [1, 2]
n = [1, 2]
print(id(m))
print(id(n))
