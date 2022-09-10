import random

td_list = [i for i in range(10)]
print("列表推导式： ", td_list)

ge_list = (i for i in range(10))
print("生成器： ", ge_list)

dic = {k: random.randint(4, 9) for k in ['a', 'b', 'c', 'd']}
print("字典推导式： ", dic)

# 多循环推导式：就是求并集
list1 = ['a', 'b', 'c']
list2 = ['x', 'y', 'z']
lst = [i + "♥" + j for i in list1 for j in list2]
print(lst)
lst = zip(list1, list2)
print(list(lst))
print(dict(lst))
