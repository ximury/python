"""
把这个数组排序，那么数组中间的值肯定是存在最多的元素
"""


def find_only(nums):
    nums = [2, 2, 3, 4, 5, 4, 4, 4, 4]
    nums = xuan_ze(nums)
    le = len(nums)
    for i in range(le):
        print(i, end=':')
        print(nums[i], end='\n')
    res = 1
    for i in range(le - 1):
        if nums[i] == nums[i + 1]:
            res += 1
            if res > le / 2:
                return nums[i], res
            if i + 1 + 1 == le:
                print(nums[i], "出现:", res)
        else:
            print(nums[i], "出现:", res)
            res = 1
    return None, None


def find_only_best(nums):
    nums = [2, 2, 3, 4, 5, 4, 4, 4, 4]
    # 会超出时间限制，选择排序效率相比于sort函数不太好
    nums = xuan_ze(nums)
    le = len(nums)
    return nums[int(le / 2)]


def xuan_ze(li):
    """
    选择排序
    :param li:待排序数组
    :return: 排序后的数组
    """
    le = len(li)
    for i in range(le):
        print(i, ':', li)
        flag = False
        # 依次交换，选出最大数放在最右侧
        # 当没有交换数字的时候，break
        for j in range(le - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                flag = True
            print(li)
        if not flag:
            break
    return li


if __name__ == '__main__':
    li = []
    number, frequency = find_only(li)
    print("多数是: " + str(number), "出现次数是：" + str(frequency))

    print(find_only_best(li))

    li = [2, 2, 3, 4, 5, 4, 4, 4, 4]
    le = len(li)
    li.sort()
    print(li[le // 2])

    print('***********************')

    li = [3, 6, 4, 1, 2, 20, 5, 0, 8, 7, 9, 12]
    print(xuan_ze(li))
