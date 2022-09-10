area_pid_list = ['53c5b1d630e1429a9f19d9c2e94b2240']
area_id_list = ['46364ae666894f2f8165cb15ee3f4902']
area_id_diff = list(
    set(area_pid_list).difference(set(area_id_list))
)
print(area_id_diff)

area_pid_list = ['53c5b1d630e1429a9f19d9c2e94b2240', 'a84dec23dd6a43158d98c1bc7b7248cd']
area_id_list = ['53c5b1d630e1429a9f19d9c2e94b2240', '46364ae666894f2f8165cb15ee3f4902']
area_id_diff = list(
    set(area_pid_list).difference(set(area_id_list))
)
print(area_id_diff)
# area_id_list1 = []
# for area_pid in area_id_diff:
#     area_id_list1.extend(area_pid_id_dict.get(area_pid))
print(area_pid_list)
print(area_id_list)
area_pid_list.extend(area_id_list)
print(area_pid_list)
area_id_list1 = list(set(area_pid_list))
print(area_id_list1)