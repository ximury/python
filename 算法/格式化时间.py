import time
from datetime2 import datetime

print('year: ', time.strftime('%Y', time.localtime()))
print('year: ', time.strftime('%y', time.localtime()))
print('month: ', time.strftime('%m', time.localtime()))
print('day: ', time.strftime('%d', time.localtime()))
print('hour: ', time.strftime('%H', time.localtime()))
print('minute: ', time.strftime('%M', time.localtime()))
print('second: ', time.strftime('%S', time.localtime()))
print('date: ', time.strftime('%D', time.localtime()))
print('h: ', time.strftime('%h', time.localtime()))
# print('s: ', time.strftime('%s', time.localtime()))
print(time.strftime('%y-%m-%d %H:%M:%S', time.localtime()))

TIME = datetime.now()
print('**', TIME.strftime("%Y.%m.%d %H-%M-%S"))
