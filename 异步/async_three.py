import asyncio

async def main():
    print("hello")
    await asyncio.sleep(1)
    print("world")

asyncio.run(main())  # 在事件循环中只有一个协程，所以没有挂起任务执行其他任务这一过程

# 运行结果先打印hello然后等待1秒打印world
