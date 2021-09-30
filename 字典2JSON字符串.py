import json

dic = {"name":"wyj"}

res = json.dumps(dic)
print(res, type(res))

new_dic = json.loads(res)
print(res, type(new_dic))