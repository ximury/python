a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def fn(a):
    return a % 2 == 1


new_list = filter(fn, a)
print(type(new_list))
new_list = [i for i in new_list]
print(new_list)

odd_res = [i for i in a if i % 2 == 1]
print(odd_res)
