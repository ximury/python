import time

test_var2 = 2


def test_var_two():
    global test_var2
    test_var2 = 22
    print(test_var2)


if __name__ == '__main__':
    test_var_two()
    time.sleep(10)
    print(test_var2)
