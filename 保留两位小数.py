a = "%.3f" % 1.3335
print(a, type(a))

# 保留一位小数
b = round(float(a), 1)
print(b)

# 保留两位小数
b = round(float(a), 2)
print(b)

A = zip(("a", "b", "c", "d", "e"), (1, 2, 3, 4, 5))
A0 = dict(A)
print(A0)
