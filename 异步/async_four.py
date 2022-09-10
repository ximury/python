import asyncio


async def work(x):  # 通过async关键字定义一个协程
    for _ in range(3):
        print('Work {} is running ..'.format(x))


coroutine_1 = work(1)  # 协程是一个对象，不能直接运行

loop = asyncio.get_event_loop()
# task = loop.create_task(coroutine_1)  # 创建一个task方式一
task = asyncio.ensure_future(coroutine_1)  # 创建一个task方式二
print(task)
# run_until_complete接受的参数是一个future对象，当传入一个协程时，其内部自动封装成task对象。
# 所谓的task对象就是Future类的子类，它保存了协程运行后的状态，用于未来获取协程的结果
loop.run_until_complete(task)
print(task)

# 创建task后，task在加入事件循环之前是pending状态
# 因为上例中没有耗时操作，task很快会完成，后面打印finished状态

print(isinstance(task, asyncio.Future))  # 验证task是Future的子类
# isinstance() 与 type() 区别：
# type() 不会认为子类是一种父类类型，不考虑继承关系。
# isinstance() 会认为子类是一种父类类型，考虑继承关系。
