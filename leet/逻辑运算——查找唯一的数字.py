def find_only(nums):
    nums = [2, 2, 3, 5, 4, 3, 4, ]
    res = 0
    for i in nums:
        res = res ^ i
    return res


if __name__ == '__main__':
    li = []
    print(find_only(li))
