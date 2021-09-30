a = 5

# 一个函数内部修改全局变量
def fn():
    global a
    a = 4


if __name__ == '__main__':
    fn()
    print(a)
