class A:
    one = 1
    two = 2


aa = A()

print(aa.one)
print(aa.__getattribute__('one'))

a, b = 2, 4
print(a, b)
cc = None
print(aa)
aa = cc
print(aa)

ls = [2, 0, 6]
x = 100
try:
    for i in ls:
        y = 100 // i
        print(y)
except:
    print('err')

x = y = z = 10
x, y, z = 6, x + 1, x + 2
print(x, y, z)
