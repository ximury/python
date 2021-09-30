import re

s = "info:xiaoZhang 33 shandong*100%"

res = re.split(r":| ", s)
print(res)
