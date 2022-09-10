li = [123, 456, 567, 789]

param = 456
if param in li:
    print(li.index(param))

li = []
if not li:
    print('[]')
else:
    print('True')

# ----------------------------

l = []
l1 = [1, 2, 3]
l2 = [3, 4, 5]
l.append(l1)
l.append(l2)
print(l)

l = []
l.extend(l1)
l.extend(l2)
print(l)

print('----------------------------')
li = [[123, 11, 'a'], [456, 22, 'b'], [567, 33, 'c'], [789, 44, 'd']]
# for i, j in li:
#     print(i)
#     print(j)
for i in range(len(li)):
    print(li[i])

a = [456, 22, 'b']
b = [666, 10, 'e']
for i in li:
    if a == i:
        li[li.index(i)] = b
print(li)

li1 = [1, 2, 3, 5, 8]
li2 = ['a', 'b', 'c', 2, 1, 5]
li3 = None
if li3 is not None:
    li3 = li3
else:
    li3 = []
li = []
li.extend(li1)
li.extend(li2)
li.extend(li3)
print(li)

print(list(set(li1).intersection(set(li2))))

print('********************')

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

li1 = li[(1 - 1) * 5: 1 * 5]
print(li1)

li2 = li[0:5]
print(li2)

li3 = ['admin']
if li3:
    print(li3)

index = li.index(5)
print(index)

try:
    a = li.index(100)
except IndexError as e:
    print(e)
    a = 10
print(a)
