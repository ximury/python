import re
# 用正则匹配出标签str里面的内容（“中国”），
# 其中class的类名是不确定的
str = '<div class="nam">中国</div>'

# .代表可有可无 *代表任意字符，(.*?)提取文本
res = re.findall(r'<div class=".*">(.*?)</div>', str)

print(res)

'''
（.*）是贪婪匹配，会把满足正则的尽可能多的往后匹配

（.*?）是非贪婪匹配，会把满足正则的尽可能少匹配
'''

test_str = "<a>哈哈</a><a>呵呵</a>"
res1 = re.findall("<a>(.*)</a>", test_str)
print("贪婪匹配: ", res1)
res2 = re.findall("<a>(.*?)</a>", test_str)
print("非贪婪匹配: ", res2)

url = 'https://sycm.taobao.com/bda/tradinganaly/overview/get_summary.json?' \
      'dateRange=2018-03-20%7C2018-03-21&dateType=recent1&device=1&token=ff25b109b&_=1521595613462'

result = re.findall(r'dateRange=(.*?)%7C(.*?)&', url)
print(result)

"""
正则表达式匹配出<html><h1>www.itcast.cn</h1></html>
"""
labels = ["<html><h1>www.itcast.cn</h1></html>", "<html><h1>www.itcast.cn</h2></html>"]
for label in labels:
      ret=re.match(r'<(\w*)><(\w*)>.*?</\2></\1>', label)
      if ret:
            print("%s 是符合要求的标签" % ret.group())
            if ret.group() == label:
                  print("******")
      else:
            print("%s 不符合要求" % label)