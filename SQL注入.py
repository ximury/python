input_name = "zs"

# 原始SQL语句
sql = 'select * from demo where name="%s"' % input_name
print(sql)

input_name = "zs; drop database demo"
sql = 'select * from demo where name="%s"' % input_name
print(sql)

# 解决SQL注入
# 通过传参数方式
params = [input_name]
sql = 'select * from demo where name="%s"' % params
print(sql)