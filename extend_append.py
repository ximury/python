list1 = [1, 5, 7, 9]
list2 = [2, 5, 6, 8]
list3 = [1, 5, 7, 9]

print(list1+list2)

list1.extend(list2)
print(list1)

list3.append(list2)
print(list3)

list1.sort(reverse=False)
print(list1)
