import ast

str = "{1: '001', 2:'002'}"
str = "{}"
print(str)
di = ast.literal_eval(str)
print(di, type(di))

dic = {1: '001', 2:'002'}
dic.__delitem__(1)
print(dic)
