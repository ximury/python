import base64


def base(string: str) -> str:
    old_str = ''
    new_str = []
    base = ''
    base64_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                   'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
                   'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                   'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']
    # 把原始字符串转换为二进制，用bin转换后是0b开头的，所以把b替换了，首位补0补齐8位
    for i in string:
        old_str += '{:08}'.format(int(str(bin(ord(i))).replace('0b', '')))
    # 把转换好的二进制按照6位一组分好，最后一组不足6位的后面补0
    for j in range(0, len(old_str), 6):
        new_str.append('{:<06}'.format(old_str[j:j + 6]))
    # 在base_list中找到对应的字符，拼接
    for l in range(len(new_str)):
        base += base64_list[int(new_str[l], 2)]
    # 判断base字符结尾补几个‘=’
    if len(string) % 3 == 1:
        base += '=='
    elif len(string) % 3 == 2:
        base += '='
    return base


str_test = "Man is distinguished, not only by his reason, but by this singular passion from other animals, which is a lust of the mind, that by a perseverance of delight in the continued and indefatigable generation of knowledge, exceeds the short vehemence of any carnal pleasure."

print(base(str_test))

temp = base64.b64decode(base(str_test))
print(temp)
print(temp.decode())

print("--------------------")
# 字符串
test1 = base64.b64decode("ew8=")
print(test1)
print(test1.decode())
by = bytes("a", "UTF-8")
print(by.hex())

print("---------------------")
a = "test encode by myself"
# 字符串转bytes
b = a.encode('utf-8')
print(b, type(b))
# bytes转字符串
c = b.decode('utf-8')
print(c, type(c))
# 截取bytes串
d = b.split(b'by ')[1]
print(d, type(d))
