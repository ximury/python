import multiprocessing

import time

from multiprocessing.dummy import Pool as ThreadPool


def process(item):
    print('正在并行for循环: ' + item.get('a1') + '-' + item.get('b1') + '\n')
    time.sleep(5)


items = []
for i in range(999):
    di = {'a1': '00000', 'b1': '99999'}
    print(i)
    di["a1"] = str(i)
    di["b1"] = str(i * 100)
    items.append(di)
print(items)
# pool = ThreadPool(processes=842)
# 默认是机器的CPU数量，最多一次性842个线程
pool = ThreadPool()
# imap 线程并发执行
# map 线程顺序执行
pool.map(process, items)
pool.close()
# 调用join之前，先调用close函数，否则会出错
# 执行完close后不会有新的线程加入到pool
# join函数等待所有线程结束
pool.join()
