# 压力测试，timeit.timeit()
import timeit


def selection_sort():
    # import random
    # gen = (random.randint(1, 100) for i in range(100))  # 产生100个 1-99 范围内的随机整数
    # L = list(gen)
    # print(L)
    L = [96, 2, 65, 23, 47, 58, 8, 48, 69, 92, 34, 83, 93, 47, 45, 55, 95, 15, 92, 24, 64, 19, 29, 55, 35, 48, 39, 29,
         63, 94, 99, 38, 50, 10, 10, 93, 74, 27, 74, 44, 29, 81, 85, 86, 74, 30, 50, 50, 12, 12, 38, 75, 41, 87, 80, 97,
         16, 48, 65, 69, 83, 71, 28, 9, 64, 69, 27, 74, 74, 86, 40, 69, 79, 79, 77, 100, 53, 72, 77, 16, 8, 36, 41, 58,
         59, 29, 46, 79, 81, 66, 8, 35, 60, 52, 2, 82, 2, 36, 79, 66]
    n = len(L)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if L[j] < L[min_index]:
                min_index = j
        if min_index != i:
            L[i], L[min_index] = L[min_index], L[i]
    return L


print('Selection sort function run 1000 times, cost: ',
      timeit.timeit('selection_sort()', 'from __main__ import selection_sort', number=1000), 'seconds.')

print('Selection sort function run 1000 times, cost: ',
      timeit.repeat(stmt='selection_sort()', setup='from __main__ import selection_sort', repeat=2, number=1000),
      'seconds.')


# [0.7887709999999999, 0.8404651999999997]


def selection_sort2():
    L = [96, 2, 65, 23, 47, 58, 8, 48, 69, 92, 34, 83, 93, 47, 45, 55, 95, 15, 92, 24, 64, 19, 29, 55, 35, 48, 39, 29,
         63, 94, 99, 38, 50, 10, 10, 93, 74, 27, 74, 44, 29, 81, 85, 86, 74, 30, 50, 50, 12, 12, 38, 75, 41, 87, 80, 97,
         16, 48, 65, 69, 83, 71, 28, 9, 64, 69, 27, 74, 74, 86, 40, 69, 79, 79, 77, 100, 53, 72, 77, 16, 8, 36, 41, 58,
         59, 29, 46, 79, 81, 66, 8, 35, 60, 52, 2, 82, 2, 36, 79, 66]
    n = len(L)
    for i in range(n):
        flag = False
        for j in range(n - i - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
                flag = True
        if not flag:
            break
    return L


print('Selection sort function run 1000 times, cost: ',
      timeit.timeit(stmt='selection_sort2()', setup='from __main__ import selection_sort2', number=1000), 'seconds.')

print('Selection sort function run 1000 times, cost: ',
      timeit.repeat(stmt='selection_sort2()', setup='from __main__ import selection_sort2', repeat=2, number=1000),
      'seconds.')

# [1.7050902, 1.6269605999999994]
