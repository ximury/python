import time

query_lst = [-60000, -6000, -600, -60, -6, 0, 6, 60, 600, 6000, 60000]
lst = []
dic = {}
# total = 10000000
total = 100
for i in range(total):
    lst.append(i)
    dic[i] = 1
start = time.time()
for v in query_lst:
    if v in lst:
        continue
end1 = time.time()
for v in query_lst:
    if v in dic:
        continue
end2 = time.time()
print("list search time : %f" % (end1 - start))
print("dict search time : %f" % (end2 - end1))

aa = [(1,), (2,), (3,)]
b = (2,)
if b in aa:
    print(True)

aa = "17238239"
print(aa[:6])

a = 1
b = None
c = 0

# 0 1 =0
# None 1 1
