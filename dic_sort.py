dic = {"name": "zs", "age": 18, "city": "BJ", "tel": "111111"}

a = sorted(dic)
print(a)

b = sorted(dic.items(), key=lambda i: i[0], reverse=True)
print(b)

print(dict(b))
