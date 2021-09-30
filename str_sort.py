s = ["ab", "abc", "a", "djiw"]

# sorted有返回值，修改的是返回值，不会修改自身
b= sorted(s, key=lambda x:len(x))
print("b: ", b)
print("s: ", s)

# sort无返回值，对本身进行修改
s.sort(key=len)
print("s: ", s)