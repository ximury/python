# 使用as_completed方法

import asyncio


async def work(x):
    for _ in range(2):
        print("Work {} is running ..".format(x))
        await asyncio.sleep(1)  # 当执行某个协程时，在任务阻塞的时候用await挂起
        print(x)
    return "Work {} is finished!".format(x)


async def main_work():
    coroutine_1 = work(1)
    coroutine_2 = work(2)
    coroutine_3 = work(3)

    tasks = [
        asyncio.ensure_future(coroutine_2),
        asyncio.ensure_future(coroutine_1),
        asyncio.ensure_future(coroutine_3),
    ]

    for task in asyncio.as_completed(tasks):  # 返回一个可迭代对象，每次返回最先完成的任务的结果
        result = await task
        print(f"The task's result is : {result}")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main_work())
