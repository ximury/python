# 1、绑定回调

import asyncio


async def work(x):
    for _ in range(3):
        print('Work {} is running ..'.format(x))
    return "Work {} is finished".format(x)


def call_back(future):
    print("Callback: {}".format(future.result()))


coroutine = work(1)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine)
print(task)
task.add_done_callback(call_back)
print(task)
loop.run_until_complete(task)  # 返回任务的结果
print(task)

# 3、在不绑定回调函数的时候，当task处于finished的状态时，可以直接读取task的result的值
print("\nThe task's result is '{}' \n".format(task.result()))

# 2、使用偏函数

import functools

def call_back_2(num, future):
    print("Callback_2: {}, the num is {}".format(future.result(), num))


coroutine = work(1)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine)
task.add_done_callback(functools.partial(call_back_2, 100))
print(task)
loop.run_until_complete(task)
print(task)
print("The task's result is '{}'".format(task.result()))