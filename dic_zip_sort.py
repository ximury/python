dic = {"name": "zs", "age": 18, "city": "BJ", "tel": "111111"}
"""
根据建对字典排序
"""
# 方法一
# 字典转 列表嵌套元组
foo = zip(dic.keys(), dic.values())
print(foo)
foo = [i for i in foo]
print(foo)

# 根据键排序
b = sorted(foo, key=lambda x: x[0])
print(b)
# 字段推导式创建新字典
new_dic = {i[0]: i[1] for i in b}
print(new_dic)

# 方法二

print(dic.items())
m = sorted(dic.items(), key=lambda x: x[0], reverse=True)
print(m)
