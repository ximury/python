import datetime

import time

t = int(time.time()).__str__()
print('1: ', t, type(t))

print('2: ', datetime.datetime.now(), type(datetime.datetime.now()))

time_stamp = int(t)
print('3: ', time_stamp, type(time_stamp))
timeArray = time.localtime(time_stamp)
# print(time.strptime(time_stamp, "%Y-%m-%d %H:%M:%S"))
otherStyleTime = time.strftime("%Y.%m.%d-%H:%M:%S", timeArray)
print('4: ', otherStyleTime, type(otherStyleTime))

print("-------------")
str_datetime = '2021-03-17 18:59:05.373805'
time1 = datetime.datetime.strptime(str_datetime, "%Y-%m-%d %H:%M:%S.%f")
print(time1, type(time1))  # 2021-03-17 18:59:05.373805 <class 'datetime.datetime'>
time2 = time1.strftime('%Y-%m-%d %H:%M:%S')
print(time2, type(time2))  # 2021-03-17 18:59:05 <class 'str'>
print("-------------")

from datetime import datetime
creation_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
print(creation_time, type(creation_time))

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
t1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(type(t1), t1)
