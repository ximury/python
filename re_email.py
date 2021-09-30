import re

# 匹配163邮箱
email_list = ["xiaoming@163.com", "xiaohong@163.comheihei", "ww.com.xiaowang@qq.com"]

for email in email_list:
    ret = re.match("[\w]{4,20}@163\.com$", email)
    if ret:
        print("ret: ", ret)
        print("%s 是符合规定的邮件地址" % ret.group())
