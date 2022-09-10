li = [1, 2, 3, 4]
li.pop()
print(li)

li = [1, 2, 3, 4]
li.pop(0)
print(li)

object_list = [(10,), (11,), (12,)]
li.extend(object_item[0] for object_item in object_list)
print(li)
