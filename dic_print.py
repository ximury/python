def fn(k, v, dic={}):
    dic[k] = v
    print(dic)


fn("one", 1)
fn("two", 2)
# 传了一个新字典，所以不再是原先默认参数的字典
fn("three", 3, {})
