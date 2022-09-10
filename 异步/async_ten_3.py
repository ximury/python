import asyncio
import time

async def work(delay, msg):
    print(f"Task receives the message :'{msg}' ")
    await asyncio.sleep(delay)
    print(msg)

async def main():
    print(f"Started at {time.strftime('%X')}")
    # 启动一个协程，等待它运行完后，继续往下执行
    # （原因是没有将协程对象加到事件循环里，所以按照程序运行方式，顺序执行）
    await work(1, "hello")  # 启动一个协程，但是这是顺序执行的
    await work(2, "world")
    await work(2, "!!!")
    print(f"Finished at time {time.strftime('%X')}")

asyncio.run(main())
# 运行结果：
# 先打印print(f"Task receives the message :'{msg}' ")然后等待1秒后打印“hello”，
# 然后再次打印print(f"Task receives the message :'{msg}' ")等待2秒后打印“world”
