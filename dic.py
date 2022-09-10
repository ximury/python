# 字典如何删除键

dic1 = {"name": "test", "age": 18}

del dic1["name"]

print(dic1)

dic1.pop("age")

print(dic1)

# 合并两个字典
dic2 = {"name": "ls"}

dic1.update(dic2)

print(dic1)

# 字典添加键值对
print("-----------------------------")
dic3 = {}
dic3['name'] = 'test'
print(dic3)
# 列表中添加字典
print(dic3.get('namew') is None)

# print(dic3['namew'])

# print(dic3.name)


dict4 = {'111': []}
if dict4.get('111') is None:
    dict4['111'] = [111]
else:
    dict4['111'].append(110)
    # dict4['111'].append('111')
print(dict4)

print('---------------------------------------')
dict5 = {'url': '', 'verification': {'111': '011', '222': '022'}}
print(dict5['verification'].keys())
if '111' in dict5['verification'].keys():
    middle = dict5['verification']['111']
    print(middle)

dict6 = {'url': ['111', '011', '222', '022']}
dict6['url'].remove('111')
print(dict6)
res = dict6.get('url1', '111')
print(res)

print('-------------------------')
res = {}
res['111'] = 11111
res['222'] = 22222
print(type(res['111']))
print(res)

for item in res:
    print(res.get(item))

dic1 = {'1': 'a', '2': 'b', '3': 'c'}
print(dic1.keys())
li = list(dic1.keys())
print(li, type(li))

for item in dic1:
    print(item, end=': ')
    print(dic1[item])
