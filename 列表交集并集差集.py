a =[1,2,3,4]
b=[4,3,1,6]
jj1=[i for i in a if i in b]
jj2 =list(set(a).intersection(set(b)))
print("交集：")
print(jj1)
print(jj2)

bj1=list(set(a).union(set(b)))
print("并集：")
print(bj1)

# b中有而a中没有
cj1=list(set(b).difference(set(a)))
# a中有而b中没有
cj2=list(set(a).difference((set(b))))
print("差集：")
print(cj1)
print(cj2)