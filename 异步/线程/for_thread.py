import multiprocessing

import time

from multiprocessing.dummy import Pool as ThreadPool


def process(item):
    print('正在并行for循环: ' + item + '\n')
    time.sleep(5)


items = ['apple', 'banana', 'cake', 'dumpling']
items = []
for i in range(999):
    items.append(str(i))
var1 = ''
for i in range(1, 5):
    var1 = '%05d' % i
print(var1)
pool = ThreadPool(processes=842)
# 默认是机器的CPU数量，最多一次性842个线程
# pool = ThreadPool()
# imap 线程并发执行
# map 线程顺序执行
pool.map(process, items)
pool.close()
# 调用join之前，先调用close函数，否则会出错
# 执行完close后不会有新的线程加入到pool
# join函数等待所有线程结束
pool.join()

