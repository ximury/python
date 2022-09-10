def f1(data={}):
    return len(data)


def show(n):
    for i in n:
        print(i)


if __name__ == '__main__':
    a = f1(data={1: 1, 2: 2})
    b = f1(data={3: 3, 4: 4, 5: 5})
    print(b)
    l = [1, 2, 3]
    l.append(l)
    print(l)
    l = [1, 2, 3, 4, 5, 6, 7]
    print(l[3:2])
    print(l[-5:-3])
    atr = 'wu23811'
    print(atr.count('1'))
    a = 1
    b = 2
    print(a > b)
    print(b.__lt__(a))
    print(1 in l)

    show((1, 2, 3))
    # show(3.4)

print("***************************")


class T:
    pa1: str


t = T()
t.pa1 = 219
print(t.pa1)
