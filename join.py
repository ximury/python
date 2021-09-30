import os

x = "abc"
y = "def"

z = ["m", "n", "p"]

print(x.join(y))
print(x.join(z))

path_a = "\\c\\test\\a"

path_b = "dir\\b"

print(os.path.join(path_a, path_b))

data1 = {'error': '发生了内部错误'}
data2 = ['第2行发生错误,原因为:更新出错']
data11 = ';\n'.join(data1)
print(data11)
data22 = ';\n'.join(data2)
print(data22)
data3 = '/ '.join(data1)
print(data3)