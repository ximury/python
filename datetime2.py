from datetime import datetime

time = datetime.now()
print(time, type(time))
print("----------------------")

time = str(time)
print(time, type(time))
print("----------------------")

time = datetime.now()
# time = "1618815060"
print(time, type(time))
time = time.strftime('%Y-%m-%d %H:%M:%S')
print(time, type(time))
