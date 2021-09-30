# 递归
import sys


def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


li = []
if __name__ == '__main__':

    for line in sys.stdin:
        # a = input()
        if not line:
            break
        a = line.split()
        print(a)
        li.append(int(a[0]))
        print(li)
    for i in li:
        print(i, type(i))
        print(fib(i))

# 输出第10个斐波那契数列
print(fib(10))


def fib_all(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


# 输出前 10 个斐波那契数列
print(fib_all(10))
