def fn(k, v, dic={}):
    dic[k] = v
    print(dic)

    print(dic.keys(), type(dic.keys()))
    if 'one' in dic.keys():
        print('可遍历')


fn("one", 1)
fn("two", 2)

# 传了一个新字典，所以不再是原先默认参数的字典
fn("three", 3, {})

res = ''
di = {"first": {"second1": {"third": [True]}}}
if "first" in di and "second" in di.get("first") and "third" in di.get("first").get("second"):
    res = len(di["first"]["second"]["third"])
print(res)

# if (
#         "cpu_stats" in old_result
#         and "cpu_usage" in old_result.get("cpu_stats")
#         and "percpu_usage"
#         in old_result.get("cpu_stats").get("cpu_usage")
# ):
