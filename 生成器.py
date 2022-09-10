# 引出生成器：里面是一个对象，保存了产生元素的算法，同时会记录游标的位置
# 创建一个生成器：1.通过列表生成式来创建；
#              2. 通过函数来创建生成器（yield）
# 遍历生成器中的元素内容：
#         1. 通过next(g)，当已经遍历生成器结尾，会抛异常StopIteration
#         2. 通过for循环来遍历
#         3. 通过object对象内置的__next__()，当已经遍历生成器结尾，会抛异常StopIteration
#         4. 调用send函数，但是生成器的第一个值必须使用send(None),后面的值就没有限制
L = [x * x for x in range(10)]

print(L)

# 没有更多的元素时，抛出StopIteration的错误
g = (x * x for x in range(10))

print(g)
print(g.__next__(), end='-\n')

g = (x * x for x in range(10))
for i in range(10):
    print(g.__next__(), end=' -- ')

print()
g = (x * x for x in range(10))
for i in g:
    print(g.__next__(), end=' --- ')

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
print(odd().__next__(), end='-\n')
print(odd().__next__(), end='--\n')
print(odd().__next__(), end='---\n')

print(o.__next__(), end='*\n')
print(o.__next__(), end='**\n')
print(o.__next__(), end='***\n')
