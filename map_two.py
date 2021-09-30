list_test = [1, 2, 3, 4, 5]


def fn(x):
    return x ** 2


res = list(map(fn, list_test))

print(res)

list_res = [i for i in res if i > 10]
print(list_res)

new_res = map(fn, list_test)
print(list(new_res), type(list(new_res)))
for i in list(new_res):
    print(i)