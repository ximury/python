from operator import mod

import phi

print(mod(32, 10))

for c in range(1, 10):
    if c ** 2 == 16:
        print(c)

c = 123612763
n = 23333 * 10007
for d in range(1, 10):
    if c ** d == 84859100:
        print(d)

print(mod(1, n))
