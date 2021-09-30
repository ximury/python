import math

a = math.pow(2, 4)
print(a)

b = 2147483647

for i in range(100):
    if math.pow(10, i) > b:
        print(i, math.pow(10, i))
        break
