import asyncio

import time


async def work(x):  # 通过async关键字定义一个协程
    for _ in range(3):
        print('Work {} is running ..'.format(x), f"Started at {time.strftime('%X')}")
        await asyncio.sleep(x)


async def main():
    coroutine_1 = work(1)  # 协程是一个对象，不能直接运行
    coroutine_2 = work(2)

    task1 = asyncio.create_task(coroutine_1)  # 将事件加入了运行队列里，可以并发运行
    task2 = asyncio.create_task(coroutine_2)
    await task1  # 并发运行
    await task2
    print("The main thread", f"Started at {time.strftime('%X')}")


asyncio.run(main())
