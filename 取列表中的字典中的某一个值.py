test = [{"var": 1, "num": 2}, {"var": 3, "num": 4}, {"var": 5, "num": 6}]

# 取出var值为5的字典中的num的值
for i in test:
    print(i)
    print(i.get("var"))
    if i.get("var") == 5:
        print(i.get("num"))

testdata = [{"var": 1, "num": 2}]
print("var: ", testdata[0].get("var"))

testdic = {"var":10, "num": 10}
print(type(testdic), testdic.get('num'))