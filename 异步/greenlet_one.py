from greenlet import greenlet
import time


def task_1():
    while True:
        print("--This is task 1!--")
        g2.switch()  # 切换到g2中运行
        time.sleep(0.5)


def task_2():
    while True:
        print("--This is task 2!--")
        g1.switch()  # 切换到g1中运行
        time.sleep(0.5)


if __name__ == "__main__":
    """
    greenlet已经实现了协程，但是这个需要人工切换，很麻烦。
    python中还有一个比greenlet更强大的并且能够自动切换任务的模块gevent，
    其原理是当一个greenlet遇到IO(比如网络、文件操作等)操作时，比如访问网络，
    就自动切换到其他的greenlet，等到IO操作完成，再在适当的时候切换回来继续执行。
    由于IO操作非常耗时，经常使程序处于等待状态，有了gevent为我们自动切换协程，
    就保证总有greenlet在运行，而不是等待IO
    """
    g1 = greenlet(task_1)  # 定义greenlet对象
    g2 = greenlet(task_2)

    g1.switch()  # 切换到g1中运行
