def range_t(start, end, step):
    cur = start
    while cur > end:
        yield cur
        cur += step
    # return cur


if __name__ == '__main__':
    start = 2
    end = 10
    step = 2
    res = range_t(start, end, step)
    # print(res)
    # for i in range(2):
    #     print(i)
    #     print(res.__next__())

    x = [1, 2]
    res = iter(x)
    print(res.__next__())
    print(res.__next__())  # --->可以简写成next(res)
    try:
        if res.__next__():  # StopIteration 无可迭代对象，迭代结束
            print(next(res))
    except Exception as e:
        raise e
    finally:
        print('Finished')
