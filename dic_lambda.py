# 列表嵌套字典排序，根据name以及age进行排序
foo = [{"name": "zs", "age": 19}, {"name": "ll", "age": 54},

       {"name": "wa", "age": 17}, {"name": "df", "age": 23}]

a = sorted(foo, key=lambda x: x['age'], reverse=True)
print(a)

b = sorted(foo, key=lambda x: x['name'])
print(b)

# 列表嵌套列表，年龄相同的处理方式（再加一个字段进行排序）
foo = [["zs", 19], ["ll", 54],

       ["wa", 17], ["df", 19]]

c = sorted(foo, key=lambda x: (x[1], (x[0])))
d = sorted(foo, key=lambda x: x[1])
print(c)
print(d)