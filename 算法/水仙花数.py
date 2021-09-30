print(348 % 100 // 10)
for i in range(100, 1000):
    a = i % 10
    b = i % 100 // 10
    c = i % 1000 // 100
    if i == a ** 3 + b ** 3 + c ** 3:
        print(a, b, c, end=' ')
        print(i)
