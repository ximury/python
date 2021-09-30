from functools import reduce


def addBinary(a: str, b: str) -> str:
    li = []
    mid = 0
    base_str = ''
    if len(a) < len(b):
        for i in range(len(b) - len(a)):
            a = '0' + a
    if len(a) > len(b):
        for i in range(len(a) - len(b)):
            b = '0' + b
    # 将字符串反转
    a = reduce(lambda x, y: y + x, a)
    b = reduce(lambda x, y: y + x, b)
    posi = -1
    for i in a:
        posi += 1
        sum = int(i) + int(b[posi]) + mid
        # sum=0或1
        if sum < 2:
            mid = 0
            li.append(sum)
        # sum=2或3
        else:
            mid = 1
            li.append(sum - 2)
    if mid == 1:
        li.append(1)

    # 将列表反转
    li.reverse()
    for i in li:
        base_str += str(i)
    return base_str


print(addBinary('11', '1'))

print("****************************")
a = "10"
b = "1"
print(a[0], a[1])
for i in a:
    print(i, a.index(i))

test1 = "1"
test2 = "2"
print(test1 + test2)
print(int(test1) + int(test2))

# for i in range(2):
#     print(i)

c = "12145"
index = 0
for i in c:
    print(i, c.__getitem__(index), c[index])
    index += 1
