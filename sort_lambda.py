list = [0, -2, -4, 9, 5, 8]

a = sorted(list, key=lambda x: x)
print(a)

foo = [-5, 8, 0, 4, 9, -4, -20, -2, 8, 2, -4]
a = sorted(foo, key=lambda x: (x < 0, abs(x)))
print(a)
