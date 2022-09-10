import re

str1 = 'dsf"safd"sfas\'fwe\'rrw\'erw\'ewwew"rsdr"sdsd'
print(str1)

# 将成对的英文双引号改为成对的中文双引号
pattern = re.compile(r'"(.*?)"')
result = pattern.findall(str1)
for l in result:
    str1 = str1.replace('"{}"'.format(l), '“{}”'.format(l))
# 将成对的英文单引号改为成对的中文单引号
pattern = re.compile(r"'(.*?)'")
result = pattern.findall(str1)
for l in result:
    str1 = str1.replace("'{}'".format(l), "‘{}’".format(l))

# 将单独的单双引号替换为空
str1 = str1.replace("'", "")
str1 = str1.replace('"', "")

print(str1)
