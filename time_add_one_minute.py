from datetime import datetime

import time

t = int(time.time())  # 1635410988

print(t)

t = t + 60

# 时间戳转时间字符串
time1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))

print(time1, type(time1))  # 2021-10-28 16:50:48  <class 'str'>

cron = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(time.time()) + 60))

print(cron)
print("***************************")
cron = "2022-05-17 14:38:43"
# 时间字符串转时间戳
a1 = int(datetime.strptime(cron, '%Y-%m-%d %H:%M:%S').timestamp())
print(a1)

t2 = time.mktime(time.strptime("2022-05-17 14:38:43", '%Y-%m-%d %H:%M:%S'))
print(t2, type(t2))
# 1652769523.0 <class 'float'>

