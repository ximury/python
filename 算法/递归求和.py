def get_sum(num):
    if num >= 1:
        res = num + get_sum(num - 1)
    else:
        res = 0
    return res


print(get_sum(10))
