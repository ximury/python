a = b'/dev/pts/1\n'
b = a.decode('utf-8')
print(b.strip())

str = '/dev/pts/1'
print("/".join(str.split('/')[2:]))

str2 = 'tty7\npts/1'
str3 = '(:0)\n(172.17.129.53)'
str2_li = str2.split('\n')
str3_li = str3.split('\n')
print(str2_li)
print(str3_li)
z1 = zip(str2_li, str3_li)
print(z1)
dic = dict(z1)
print(dic)