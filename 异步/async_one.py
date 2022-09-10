def fun1(length, a):
    b = a
    for i in range(length):
        a += 1
        print("value of a before: " + str(b) + " now it's " + str(a))
    return a


def main1():
    r1 = fun1(50000, 0)
    r2 = fun1(100, 12)
    r3 = fun1(100, 41)


import asyncio


async def fun2(length, a):
    b = a
    for i in range(length):
        a += 1
        if i % 10000 == 0:
            await asyncio.sleep(0.0001)
        print("value of a before: " + str(b) + " now it's " + str(a))
    return a


async def main2():
    """
    通过async定义一个协程，协程是一个对象，不能直接运行，
    需要把协程加入到事件循环（loop）中，由loop在适当的时候调用协程
    """
    # creating subroutines.
    t1 = loop.create_task(fun2(20000, 0))
    t2 = loop.create_task(fun2(100, 100))
    t3 = loop.create_task(fun2(100, 500))

    await asyncio.wait([t1, t2, t3])


if __name__ == "__main__":
    # main1()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main2())

    loop.close()
