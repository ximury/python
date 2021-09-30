from datetime import datetime

import time

time1 = time.time()

time2 = time.time()

print(time1)

print(time2)

print(time2 - time1 < 10)

time1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
print(time1, type(time1))

time2 = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(time2, type(time2))
