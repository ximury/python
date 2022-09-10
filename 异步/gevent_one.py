import gevent


def task_1(num):
    for i in range(num):
        print(gevent.getcurrent(), i)
        gevent.sleep(1)  # 模拟一个耗时操作，注意不能使用time模块的sleep


if __name__ == "__main__":
    g1 = gevent.spawn(task_1, 5)  # 创建协程
    g2 = gevent.spawn(task_1, 5)
    g3 = gevent.spawn(task_1, 5)

    g1.join()  # 等待协程运行完毕
    g2.join()
    g3.join()
