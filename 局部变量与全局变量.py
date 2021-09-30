# 全局变量
x = 50
str = 'str'
dt = {'1': 'one'}
li = []
'''
函数内部无法操作全局变量（包括列表），但是可以操作字典
'''


def func(x, str, dt, li):
    print('局部变量x={}, str={}, dt={}, li={}'.format(x, str, dt, li))
    x = 2
    str = 'string'
    dt['1'] = '1'
    li = [1]
    print('局部变量x={}, str={}, dt={}, li={}'.format(x, str, dt, li))


func(x, str, dt, li)
print('全局常数变量x=', x)
print('全局字符串变量str=', str)
print('全局字典变量dt=', dt)
print('全局列表变量li=', li)

# func(x, 'string', dt, li)
# print(dt)
# print(li)

print('-----------------------')
# 局部列表修改全局列表
dict_list = {1: []}


def func(li):
    dict_list[1] = li


func([1, 2])
print(dict_list)
func([3, 4])
print(dict_list)

print('-------------------------------------')
y = True


def check_key():
    global y
    y = False


check_key()
print('全局变量y：', y)
