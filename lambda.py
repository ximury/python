# 由于lambda只是一个表达式，(匿名函数)
# 所以它可以直接作为list和dict的成员
sum = lambda a, b: a * b
print(sum(5, 4))

a = ["test", "", "nice", "", "china", "really", "真", ""]
res = list(map(lambda x:"填充" if x=="" else x, a))
print(res)
print(a)