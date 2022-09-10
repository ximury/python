a = '  hehehe '

print(a.strip())

b = '   '

print(b.isspace(), end=" is space \n")
print(b.strip() == '')

c = ''

print(c.strip() == '')

d = ' ae'
print(d.startswith(' '), end=' start is space \n')
print(d.endswith(' '), end=' end is space \n')

str1 = "swe.w.des"
str2 = str1.strip('.des')
print(str2)
