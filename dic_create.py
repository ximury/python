# 列表
s = dict([["name", "zs"], ["age", 18]])

print(s)

# 元组
s = dict([("name", "zs"), ("age", 18)])
print(s)

conn = {}
conn['1.1.1.1'] = 6080
conn['1.1.1.2'] = 6081
conn['1.1.1.3'] = 6082

print(conn)
for i in conn:
    if conn.get(i) == 6081:
        print("deleting...")
        del conn[i]
        break
print(conn)

if conn.get('1.1.1.1') is not None:
    print("is not none")

dict_list = {}
nonelist = []

if nonelist:
    print("**not none")
else:
    print("**none")

# dict_list['1.1.1.1'].append(30)  # 空字典无法append
# print(dict_list)
# dict_list['1.1.1.1'] = [100]
# print(dict_list)
# dict_list['1.1.1.1'].append(200)
# print(dict_list)

dict_list['2.2.2.2'] = ['yes']
if dict_list.get('2.2.2.2') is None:
    dict_list['2.2.2.2'] = ['file_name']
else:
    dict_list['2.2.2.2'].append('file_name')
print(dict_list)

data = []
data = dict_list.get('3.3.3.3')
print(data)

print("****************************")
di = {}
start = [1, 2, 3, 2]
for item in start:
    di.setdefault(item, [])
    di[item].append(item * 100)
print(di)
