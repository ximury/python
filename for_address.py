area_host_dict = {}
area = 'a1'

for i in range(2):
    added_host_list = [1,2]
    if area_host_dict.get(area) is not None:
        # area_host_dict[area] = area_host_dict[area]+added_host_list
        area_host_dict[area] += added_host_list
        print(added_host_list)
        area_host_dict[area] = list(area_host_dict[area])
    else:
        area_host_dict[area] = added_host_list
        print(added_host_list)
print(area_host_dict)