import copy

a = "test"
b = a
c = copy.copy(a)
d = copy.deepcopy(a)
print(a, id(a))
print(b, id(b))
print(c, id(c))
print(d, id(d))

list = [1, 2, [3, 4]]
l1 = copy.copy(list)
l2 = copy.deepcopy(list)

# 不一样的ID
print(list, id(list))
print(l1, id(l1))
print(l2, id(l2))

# print("******")
# list[0] = 10
# print(list, id(list))
# print(l1, id(l1))
# print(l2, id(l2))

print("******")
# list[2] = [30,40]
# print(list, id(list))
# print(l1, id(l1))
# print(l2, id(l2))

list[2][0] = 100
print(list, id(list))
print(l1, id(l1))
print(l2, id(l2))
