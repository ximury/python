import re

str = "小明年龄18岁，工资10k"

# search匹配到第一个匹配的数据
res = re.search(r"\d+", str).group()
print("search结果", res)

res = re.findall(r"\d+", str)
print("findall结果", res)

# 匹配以“小明”开头的字符串
res = re.match("小明", str).group()
print("match结果", res)

# str字符串不是以工资开头，所以匹配报错
res = re.match(r"\d+", str)
print("Error, 不加group为none,匹配不到", res)

res = re.match("工资", str).group()
print("match结果", res)
