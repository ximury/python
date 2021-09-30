import time

time_stamp = 1618815060

timeArray = time.localtime(time_stamp)
# print(time.strptime(time_stamp, "%Y-%m-%d %H:%M:%S"))
otherStyleTime = time.strftime("%Y.%m.%d-%H:%M:%S", timeArray)
print(otherStyleTime, type(otherStyleTime))