area_host_dict = {}
added_host_list = ["a.b.c", "b.c.d"]
area = 'a1'

for i in range(2):
    print(i)
    if area_host_dict.get(area) is not None:
        print(added_host_list)
        area_host_dict[area] += added_host_list
    else:
        print(added_host_list)
        area_host_dict[area] = added_host_list

# area_host_dict[area] = added_host_list

print(area_host_dict)