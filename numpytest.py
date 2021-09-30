import numpy as np
online_num_list_tmp = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2,
 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
 3, 3, 3, 3, 3, 3, 3, 10, 3, 3, 3, 3, 3, 3,
 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2,
 2, 2, 2, 3, 3, 5, 3, 3, 3, 3, 3, 3, 3, 3,
 3, 3, 3, 3, 3, 3, 3, 3, 3]
min_size = len(online_num_list_tmp)
print(online_num_list_tmp[-min_size:])
online_num_list_tmp = np.array(online_num_list_tmp[-min_size:])
print(online_num_list_tmp)

arr = [1, 4, 3, 2, 10, 30, 16]
l = len(arr)
print(arr[-2:])
print(arr[-l:])