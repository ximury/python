i = int(input('净利润：'))
arr = [1000000, 600000, 400000, 200000, 100000, 0]
rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
total = 0
for index in range(0, 6):
    print(arr[index])
    if i > arr[index]:
        total += (i - arr[index]) * rat[index]
        print('单块利润：', (i - arr[index]) * rat[index])
print(total)
