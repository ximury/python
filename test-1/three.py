class Hello():
    pass

a = Hello()
a.__dir__()
a.__hash__()

a = """idiwieew"""
print(a)

a = '''111'''
print(a)

def cha(list):
    list.append("end")
    print("list", list)
strs = ["1", "2"]
cha(strs)
print("strs", strs)

# c =eval("3*4")
# print(c, type(c))
d= 6
# d1 = input(6)
# print(d1, type(d1))
def cha(q):
    return q*2
print(cha(2))