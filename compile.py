str_test = "for i in range(0,10): print(i, end= ' ')"

# compile将字符串编译为字节代码对象
c = compile(str_test, '', 'exec')

exec(c)

# eval执行一个字符串表达式，并返回表达式的值
str_calculate = "4 + 5"

d = compile(str_calculate, '', 'eval')

print(eval(d))

