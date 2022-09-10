#!/usr/bin/python3

import threading
import time

exitFlag = 0


class MyThread(threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay

    def run(self):
        print("开始线程：" + self.name)
        print_time(self.name, self.delay, 5)
        print("当前线程：{}".format(threading.currentThread()))
        print(threading.enumerate())
        print("退出线程：" + self.name)


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


# 创建新线程
thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
print("当前线程1：{}".format(threading.currentThread()))
thread2.start()
print("当前线程2：{}".format(threading.currentThread()))
thread1.join()
thread2.join()
print(threading.enumerate())
print("退出主线程")

