import re

a = "张明 90 score"

# sub替换
ret = re.sub(r"\d+", "100", a)
print(ret)
