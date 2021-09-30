def find_only(nums, target):
    if not nums or len(nums) == 0:
        return False
    m, n = len(nums), len(nums[0])
    row, col = m - 1, 0  # 左下角开始查找，即第m行，第1列
    while row >= 0 and col < n:
        if target == nums[row][col]:
            return True
        elif target > nums[row][col]:
            col += 1
        elif target < nums[row][col]:
            row -= 1
    return False


if __name__ == '__main__':
    li = [[1, 4, 7, 11, 15],
          [2, 5, 8, 12, 19],
          [3, 6, 9, 16, 22],
          [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]]
    target = 9
    print(find_only(li, target))
