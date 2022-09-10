from collections import defaultdict

dic = {"name": "zs", "age": 18, "city": "BJ", "tel": "111111"}

if dic.get("name") and dic.get("age1"):
    print(True)
else:
    print(False)

print("***************************")
# set default

dic1 = {}
dic1[3] = "c"

for item in range(1, 5):
    dic1.setdefault(item, 'A')
print(dic1)

print("***************************")
# dic2 = defaultdict(lambda: 1)
dic2 = defaultdict(int)
for item in range(1, 5):
    dic2[item] += 10 + item
print(dic2)
print(dic2.get(1))

dic2.pop(2)
print(dic2)
print(dict(dic2))

print("***************************")
a = [1, 2, 3]
a.remove(4) if 4 in a else None
print(a)

