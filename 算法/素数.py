from math import sqrt

h = 0
leap = 1

for i in range(101, 201):
    leap = 1
    k = int(sqrt(i + 1))
    for j in range(2, k + 1):
        # 不是素数
        if i % j == 0:
            leap = 0
    if leap == 1:
        h += 1
        print(i, end=' ')
        if h % 5 == 0:
            print()

print('\n总共有%d个素数' % h)
