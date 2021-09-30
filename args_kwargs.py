# kwargs(keyword arguments)在args之后表示成对键值对
def foo(*args, **kwargs):
    print('args = ', args)
    print('kwargs = ', kwargs)
    print('*********************')


if __name__ == '__main__':
    foo(1, 2, 3)
    foo(a=1, b=2, c=3)
    foo(1, 2, 3, a=1, b=2, c=3)
    foo('a', 1, None, a=1, b='b', c=None)
