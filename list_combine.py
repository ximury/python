import operator

a = [[1, 2], [2, 3], [5, 6]]

x = [j for i in a for j in i]
print(x)

# numpy矩阵
import numpy as np

b = np.array(a).flatten().tolist()
print(b)

file_list = ['123', '345', '445', '187']
le = len(file_list)
print(type(le))
print(file_list[1:le])

file_list.sort(reverse=True)
print(file_list)

file_list = [{'name': '123', 'size': 80},
             {'name': '117', 'size': 110},
             {'name': '233', 'size': 300},
             {'name': '199', 'size': 100}]
file_list = sorted(file_list, key=lambda x: x['name'])
print(file_list)

file_list = sorted(file_list, key=operator.itemgetter('name'))
print(file_list)

print('-----')
print(file_list+file_list)
print(file_list)
