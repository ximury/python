def test_fun1(item, li=[]):
    li.append(item)
    return li


print(test_fun1('a'))

print(test_fun1('b'))

print(test_fun1('c'))


def test_fun2(item, li=None):
    if li is None:
        li = []
    li.append(item)
    return li


print(test_fun2('a'))

print(test_fun2('b'))

print(test_fun2('c'))
