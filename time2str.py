# encoding: utf-8
import datetime

timestamp = '2021-11-02T08:56:13.001Z'
day = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
print(day)
print(type(day))
day = datetime.datetime.strftime(day, '%Y-%m-%d %H:%M:%S')
print(day)
print(type(day))

print('++++++++++++++++++++++++++++++++++++++++++++')
from datetime import datetime

day = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y-%m-%d %H:%M:%S')
print(day)  # 2021-11-02 08:56:13
print(type(day))  # <class 'str'>

print('--------------------------------------------')

import time

timestamp = '2021-11-02T08:56:13.001Z'
time.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')  # linux python3.8无法使用
print(day)  # 2021-11-02 08:56:13
print(type(day))  # <class 'str'>

print('==============================')
import datetime

timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(timestamp, type(timestamp))
new_time = datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
print(new_time, type(new_time))

from datetime import datetime

t = datetime.strptime(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S').timestamp()
print(t, type(t))

print("*********************************")
from datetime import datetime

t1 = datetime.now()
print(t1, type(t1))
# 2022-05-17 11:26:58.033436 <class 'datetime.datetime'>

t2 = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(t2, type(t2))
# 2022-05-17 11:29:06 <class 'str'>

t3 = datetime.strptime('2022-05-17 11:29:06', '%Y-%m-%d %H:%M:%S')
print(t3, type(t3))
# 2022-05-17 11:29:06 <class 'datetime.datetime'>

t4 = datetime.strptime(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
print(t4, type(t4))
# 2022-05-17 11:32:44 <class 'datetime.datetime'>

t5 = datetime.now().timestamp()
print(t5, type(t5))
# 1652758498.971751 <class 'float'>

t6 = datetime.strptime(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S').timestamp()
print(t6, type(t6))
# 1652758879.0 <class 'float'>

import time

t1 = time.localtime()
print(t1, type(t1))
# time.struct_time(tm_year=2022, tm_mon=5, tm_mday=17, tm_hour=13, tm_min=55, tm_sec=49, tm_wday=1, tm_yday=137, tm_isdst=0) <class 'time.struct_time'>
t2 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(t2, type(t2))
# 2022-05-17 13:55:49 <class 'str'>

time_stamp = 1658456151
t1 = time.localtime(time_stamp)
print('***', t1, type(t1))
# time.struct_time(tm_year=2022, tm_mon=5, tm_mday=17, tm_hour=13, tm_min=59, tm_sec=29, tm_wday=1, tm_yday=137, tm_isdst=0) <class 'time.struct_time'>
t2 = time.strftime("%Y.%m.%d-%H:%M:%S", t1)
print(t2, type(t2))
# 2022.05.17-13:59:29 <class 'str'>

t3 = time.time()
print(t3, type(t3))
# 1652767464.013739 <class 'float'>

import time
from datetime import date

t1 = int(time.mktime(date.today().timetuple()))
print(t1, type(t1))
# 1652716800 <class 'int'>

t1 = date.today().timetuple()
print(t1, type(t1))

t3 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(time.time()) + 60))
print(t3, type(t3))
# 2022-05-17 14:41:56 <class 'str'>


'{ ##### $(who am i |awk "{print \$1\" \"\$2\" \"\$5}")  #### $(id|awk "{print \$1}") #### $(history 1 | { read x cmd; echo "$cmd"; }); } >>$HISTORY_FILE'