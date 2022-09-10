def a(param, **kwargs):
    print(param)
    if kwargs.get("num"):
        print(True)
    b(**kwargs)


def b(**kwargs):
    if kwargs.get("num"):
        print(True)


if __name__ == '__main__':
    a(2, num=10)
