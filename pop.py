from datetime import datetime

li = [1, 2, 3, 4]
li = []
if li:
    res1 = li.pop()
    print(res1)
print(li)

di = {'a': 1, 'b': 2}
di['a1'] = di.pop('a')
print(di)

a = datetime.now().timestamp()
print(a)
a, b, c, d = 1, 2, 3, 4
print(a, b, c, d)