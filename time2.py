from datetime import datetime

import time

time1 = time.time()  # 1635410850.4176273

time2 = time.time()

print(time1)

print(time2)

print(time2 - time1 < 10)  # True

time1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
print(time1, type(time1))  # 2021-10-28 16:47:30 <class 'str'>

time2 = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(time2, type(time2))  # 2021-10-28 16:47:30 <class 'str'>

print(datetime.now())

print(datetime.now().timestamp())

# 获取当天凌晨时间戳
from datetime import date

today_stamp = int(time.mktime(date.today().timetuple()))
print(today_stamp)
print(type(today_stamp))

# 时间戳转时间字符串
time1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(today_stamp))
print(time1)

# 获取当前时间戳
time2 = int(datetime.now().timestamp())
print(datetime.now().timestamp())
print(time2)

time3 = datetime.now()
print(time3)

time4 = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
print(time4, type(time4))
time5 = datetime.strptime(time4, "%Y-%m-%d %H:%M:%S")
print(time5, type(time5))
time6 = time5.timestamp()
print(time6, type(time6))
