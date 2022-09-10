str = "123\n456\n "

lt1 = str.split('\n')

lt2 = str.split()

print(lt1)
print(lt2)

str_none = ''

if str_none:
    print("*****************")

if len(str_none):
    print('str_none is not none')
else:
    print('str_none is none')

str1 = 'str'
str2 = 'str'
print(str1 is str2)
print(str1, end='...')
print(len('S'), end='\n---------------\n')

str3 = b'str'
print(type(str3), len(str3))
print(str3, end='***\n')

str3 = str3.decode()
print(type(str3), len(str3))
print(str3, end='***\n')

str = 'abc.kim.local'
print(str.endswith('kim.local'))

print('-------------------')
print('192.188.20.216' > '192.188.20.22')

print('-------------------')
str1 = '======================'
print(len(str1))

