import functools

dict1 = [('123',), ('234',), ('345',)]
last = []
for i in dict1:
    last.append(i[0])
print(last)


def list_unpack(l):
    """拆开一层嵌套列表元组"""
    return functools.reduce(lambda x, y: x + y, l)


def result(param):
    return [param, type(param)]


res = list_unpack(dict1)
print(result(dict1))
print(result(res))
print(result(last))
print('-----------')
print(result(list(res)))
print(result(tuple(last)))
