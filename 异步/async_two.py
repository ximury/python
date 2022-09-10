import asyncio


async def work(x):  # 通过async关键字定义一个协程
    for i in range(3):
        print('{} Work {} is running ..'.format(i, x))


coroutine_1 = work(1)  # 协程是一个对象，不能直接运行

if __name__ == '__main__':
    """
    python 3.7 以前的版本调用异步函数的步骤：
        1、调用asyncio.get_event_loop()函数获取事件循环loop对象
        2、通过不同的策略调用loop.run_forever()方法或者loop.run_until_complete()方法执行异步函数
    python3.7 以后的版本使用asyncio.run即可：
        此函数总是会创建一个新的事件循环并在结束时关闭之
        它应当被用作 asyncio 程序的主入口点，理想情况下应当只被调用一次
    """
    # 方式一：
    loop = asyncio.get_event_loop()  # 创建一个事件循环
    result = loop.run_until_complete(coroutine_1)  # 将协程对象加入到事件循环中，并执行
    print(result)  # 协程对象并没有返回结果，打印None
    # loop.close()

    # 方式二：
    # 创建一个新的事件循环，并以coroutine_1为程序的主入口，执行完毕后关闭事件循环
    # asyncio.run(coroutine_1)
