import asyncio
import time


async def work(delay, msg):
    print(f"Task receives the message :'{msg}' ")
    print("----1----")
    await asyncio.sleep(delay)
    print("----2----")
    print(msg)


async def main():
    task1 = asyncio.create_task(work(1, "hello"))
    task2 = asyncio.create_task(work(3, "world"))
    print(f"Started at {time.strftime('%X')}")
    await task1  # 此时并发运行task1和task2
    print("----3----")
    await task2
    print("----4----")
    print(f"Finished at time {time.strftime('%X')}")


asyncio.run(main())

# 运行结果说明，首先asyncio.run(main())创建一个事件循环，并以main为主要程序入口，
# 在main中，
# 1、创建俩个任务task1和task2，并加入到事件循环中，
# 2、打印Started at 11:16:08
# 3、执行await task1，此时是并发运行了task1和task2了，
