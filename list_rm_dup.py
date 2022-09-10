# 列表去重
list_test = [11, 12, 13, 12, 14, 15, 15, 16]

a = set(list_test)

print(a)

b = list(list_test)

print(b)

# 不换行打印
for i in a:
    print(i, end=" ")

print("-------------")
n = 10
list_a = [0] * n

print(list_a)

# 遍历
list_test1 = [11, 12, 13, 12, 14, 15, 15, 16]
for item in list_test1:
    if item == 12:
        list_test1.remove(item)

print(list_test1)

list_test3 = [11, 12, 13, 12, 14, 15, 15, 16]
list_test4 = [11, 12, 13, 12, 14, 15, 15, 16]
print(list_test3 == list_test4)

list_test5 = []
list_test5 = list_test4
print(list_test5)

# list去重
list_test = [11, 12, 13, 12, 14, 15, 15, 16]

a = list(set(list_test))
print(a)

print("***********************")

object_id_list = []
object_id_list.append("11")
print(object_id_list)
object_id_list = list(set(object_id_list))
print(object_id_list)


# 空list去重
list_test = []
a = list(set(list_test))
print(a)