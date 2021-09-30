import re

# 正则匹配不是以4和7结尾的手机号
tels = ["18389128994", "18937290278", "23929088973", "10039", "2910837", "19927948927", "2893u92b"]

for tel in tels:
    ret = re.match("1\d{9}[0-3,5-6,8-9]", tel)
    if ret:
        print("GET success: ", ret.group())
    else:
        print("%s is not!" % tel)