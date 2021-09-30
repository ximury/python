L = [x * x for x in range(10)]

print(L)

# 没有更多的元素时，抛出StopIteration的错误
g = (x * x for x in range(10))

print(g)
# print(g.__next__(), end=' ')

g = (x * x for x in range(10))
for i in range(10):
    print(g.__next__(), end=' ')

print()
g = (x * x for x in range(10))
for i in g:
    print(g.__next__(), end=' ')

print()
g = (x * x for x in range(10))
for i in g:
    print(i, end=' ')

print()


# generator的函数，在每次调用next()的时候执行，
# 遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 2
    print('step 3')
    yield 3


o = odd()
print(odd().__next__())
print(odd().__next__())
print(odd().__next__())

print(o.__next__())
print(o.__next__())
print(o.__next__())
