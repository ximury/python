
fp = open('./test.txt', 'w')
fp.write('hello')
fp.close()

# 使用了with以后相当于帮我们实现了文件的关闭的操作
with open('./test.txt', 'w', encoding='utf-8') as fp:
    fp.write('with')
