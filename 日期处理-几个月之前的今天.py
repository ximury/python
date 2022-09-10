import arrow

now = arrow.now()
print(now, type(now))
# 获取上个月时间
# last_month = now.shift(months=-2)
last_month = now.shift(months=-6)
print(last_month)
last_month = str(last_month)[:10]  # 只取日期部分
print(last_month)

print('-------------------')
a = '2021-12-07'
b = '2022-06-07'
print(a < b)

a = 'cluster-monitor.log.2022-03-30'
b = 'cluster-monitor.log.2022-04-30'
print(a < b)
