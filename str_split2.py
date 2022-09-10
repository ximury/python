domain = 'a.b.c'
num = '0'
domain1 = ''
print(domain.split('.')[0])
print(domain.find('a'))
if domain.find('.') != -1:
    str = domain.split('.')
    print(str)
    print(str[0] + num)
    str[0] = str[0] + num
    domain1 = '.'.join(str)
print(domain1)
print(domain)

print("------------------------1end")

domain = 'a.a.c'
if domain.find('.') != -1:
    str = domain.split('.')
    print(str)
    print(domain)
    domain1 = domain.replace(str[0], str[0] + num)

print(domain1)
print(domain)

print("------------------------2end")

domain = 'a'
str = domain.split('.')
print(str)
print(str[0] + num)
str[0] = str[0] + num
domain1 = '.'.join(str)
print(domain1)
print(domain)
