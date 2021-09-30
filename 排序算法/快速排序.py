import timeit


def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def res():
    # arr = [10, 7, 8, 9, 1, 5]
    arr = [96, 2, 65, 23, 47, 58, 8, 48, 69, 92, 34, 83, 93, 47, 45, 55, 95, 15, 92, 24, 64, 19, 29, 55, 35, 48, 39, 29,
         63, 94, 99, 38, 50, 10, 10, 93, 74, 27, 74, 44, 29, 81, 85, 86, 74, 30, 50, 50, 12, 12, 38, 75, 41, 87, 80, 97,
         16, 48, 65, 69, 83, 71, 28, 9, 64, 69, 27, 74, 74, 86, 40, 69, 79, 79, 77, 100, 53, 72, 77, 16, 8, 36, 41, 58,
         59, 29, 46, 79, 81, 66, 8, 35, 60, 52, 2, 82, 2, 36, 79, 66]
    l = len(arr)
    quick_sort(arr, 0, l - 1)
    print("排序后的数组：")
    print(arr)


if __name__ == '__main__':
    res()

print('Selection sort function run 1000 times, cost: ',
      timeit.repeat(stmt='res()',
                    setup='from __main__ import res', repeat=2, number=1000),
      'seconds.')

# [0.24309609999999998, 0.26000819999999997]