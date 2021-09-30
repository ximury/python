import re
"""
正则表达式匹配第一个URL
"""
s = '<img data-orig' \
    'inal="https://www.cnblogs.com/roadwide/p/10539910.html" ' \
    'src="https://itudo.cn/" style="display: inline;">'

res = re.findall(r"https://.*?\.html", s)[0]

print(res)

print("************")
# .*贪婪匹配， .*?非贪婪匹配
res= re.search(r"https://.*/", s)
print(res.group())