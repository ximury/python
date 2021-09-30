import re

"""
匹配中文，不包含标点符号
"""
title = '你好，hello, world, 我的世界'

pattern = re.compile(r'[\u4e00-\u9fa5]+')

result = pattern.findall(title)

print(result)
