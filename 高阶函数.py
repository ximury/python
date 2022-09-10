# 定义一个函数，传入一个列表[1,2,3,4,5,6,7],
# 返回一个新的列表[原列表每个数字的阶乘][1!,2!,3!,4!,5!,6!,7!]
# 一个阶乘函数
def test1(num):
    if num == 1:
        return 1
    else:
        return num * test1(num - 1)


# test2就是高阶函数，它的参数其中第二个参数是函数本身
def test2(num_list, func):
    new_list = []
    for x in num_list:
        new_list.append(func(x))
    return new_list


list1 = [1, 2, 3, 4, 5, 6, 7]
print(test2(list1, test1))

print("**************************")

# 内置高级函数

# 1. map：把一个可迭代对象中的每个元素转换成一个新的对象，最后返回一个迭代器
list1 = [1, 2, 3, 4, 5, 10, 6, 8, 20, 4]
it1 = map(lambda x: x ** 2, list1)  # x是列表中的每个元素
# print(it1.__next__())
print(next(it1))
print(list(it1))
# 2. reduce:把一个可迭代对象中每个元素做聚合处理，最后返回一个聚合之后的值
from functools import reduce

print(reduce(lambda x, y: x + y, list1), end='*\n')  # list1元素累加


def get_max(x, y):
    if x > y:
        return x
    else:
        return y


print(reduce(get_max, list1), end='**\n')  # 当前列表中的最大值 20
print(lambda x, y: x if x > y else y, list1)
print(reduce(lambda x, y: x if x > y else y, list1), end='**\n')  # 当前列表中的最大值 20
print(list(map(lambda x, y: x if x > y else y, list1)), end='**\n')
# print(list(reduce(get_max, list1)), end='$\n')

# 3.filter 把一个可迭代对象中的元素做过滤操作，如果func返回值为True则留下，否则过滤掉
emps = [
    {'name': 'zhangsan', 'age': 18, 'salary': 3000},
    {'name': 'lisi', 'age': 28, 'salary': 1000},
    {'name': 'wangwu', 'age': 38, 'salary': 6000}
]
# 需求，请过滤留下大于18岁的员工,返回一个迭代器
print(list(filter(lambda x: x['age'] > 18, emps)))
# 4. max和min
# 计算薪资最高的员工
print(max(emps, key=lambda x: x['salary']))
# 计算薪资最少的员工
print(min(emps, key=lambda x: x['salary']))
# 5.sorted:把一个可迭代对象里面的每个元素做排序，返回一个列表
# 根据员工的年龄降序排序
print(sorted(emps, key=lambda x: x['age'], reverse=True))
