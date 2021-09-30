a = [{'001': '001', '002': '002'}]
print(a, type(a))
a = a.__str__()
print(a, type(a))

print(['------------------'])

init_list = [0 for n in range(10)]
init_list2 = [0] * 10
print(init_list)
print(init_list2)

# list - replace
a = ['110', '111', '112', '113']

for i in a:
    print(i, a.index(i))
    if i == '112':
        id = a.index(i)
        print(a[id])
        i = i.replace('112', '000')

        a[id] = '000'
print(a)
