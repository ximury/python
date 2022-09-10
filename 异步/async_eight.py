# 简单等待的案例，貌似有问题！！！

import asyncio

async def foo():
    return 42

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # task = loop.create_task(foo())
    # print(task)
    # result = loop.run_until_complete(task)
    # print(result)
    # loop.close()
    # 注意：1、这里传递的要是一个任务组，而不能是单个task，
    #         如果只有一个任务，可以这样传递：[task](task,){task}
    #       2、直接传递协程对象的方式已弃用 即：done, pending = await asyncio.wait([foo()])
    task = loop.create_task(foo())
    print(task)
    # done, pending = await asyncio.wait((task, ))
    #
    result = loop.run_until_complete(asyncio.wait([task]))
    print(result)
    print(result[0], type(result[0]))
    for item in result[0]:
        print(item)
        print(item.result())
    # if task in done:
    #     print(f"The task's result is {task.result()}")
