list_test = [1, 2, 3, 4, 5]


def fn(x):
    return x ** 2


res = map(fn, list_test)

print(res)

print(list(res))

# res = [1,4,9,16,25]

list_res = [i for i in list(res) if i > 10]
print(list_res)

print("******")
a=list(res)
print(a)
list_res = [i for i in list(res) if i > 10]
# lambda 是一个匿名函数
# list_res = filter(lambda i: i > 5, res)
print(list_res)


# 利用map()函数，把一个list（包含若干不规范的英文名字）
# 变成一个包含规范英文名字的list
def format_name(s):
    s1 = s[0:1].upper() + s[1:].lower()
    return s1


list_name = ['admin', 'LiSart', 'Ypru']
print(list(map(format_name, list_name)))

print(list_name[1])
