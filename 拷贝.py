import copy

dic1 = {'1': 123, '2': 234, '10': {'a': 'qwe'}}
dic2 = dic1
dic3 = copy.copy(dic1)

dic1['3'] = 377
dic1['10'] = {'a': '888'}
# ------------------------------------

dic1 = [1, (2, 3), {1: 23}]
dic2 = dic1
dic3 = copy.copy(dic1)

dic1[0] = 'asd'
dic1[2][1] = 'cde'
# ------------------------------------

dic1 = {'1': 123, '2': 234, '10': {'a': 'qwe'}}
dic2 = dic1
dic3 = copy.deepcopy(dic1)

dic1['3'] = 377
dic1['10'] = {'a': '888'}
# ------------------------------------

dic1 = [1, (2, 3), {1: 23}]
dic2 = dic1
dic3 = copy.deepcopy(dic1)

dic1[0] = 'asd'
dic1[2][1] = 'cde'
# ------------------------------------

print(dic1)
print(dic2)
print(dic3)


