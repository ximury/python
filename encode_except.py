a = "test encode by myself 你好"
# 字符串转bytes
b = a.encode('utf-8')
print(b, type(b))
# bytes转字符串
ty = ""
try:
    b.decode('utf-8')
    ty = "utf-8"
    print(ty, end="-\n")
except UnicodeError:
    try:
        b.decode("gbk")
        ty = "gbk"
        print(ty, end="--\n")
    except UnicodeError:
        print("解码错误")
c = b.decode(ty)
print(c, type(c))
