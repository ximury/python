# 自定义异常

def fn():
    try:
        for i in range(5):
            if i > 2:
                raise Exception("数字不能大于2！")
            if i > 3:
                raise Exception("数字不能大于3！")
    except Exception as ret:
        print(ret)


fn()
