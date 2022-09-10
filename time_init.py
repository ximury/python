import time

t1 = 1650816000
t1 = 1654099200
t2 = time.strftime("%Y.%m.%d", time.localtime(t1))

# t2 = t1.strftime('%Y-%m-%d %H:%M:%S')

print(t2)

day_seconds = 24 * 3600
t1 = 1650816002
curr_day = t1 // day_seconds

print(curr_day)