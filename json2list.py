import json

l = ['ironpython', [1, 2, 3], {'name': 'xiaoping'}]
# json.dumps 将列表转化为json字符串
encoded_json = json.dumps(l)
print(repr(encoded_json))
print(encoded_json, type(encoded_json))
# json.loads 将json字符串读取为列表
decode_json = json.loads(encoded_json, strict=True)
print(decode_json, type(decode_json))

# ----------------------------------

l = {'001': '001', '002': '002'}
# json.dumps 将字典转化为json字符串
dic = json.dumps(l)
print(dic, type(dic))
# json.loads 将json字符串读取为字典
l_new = json.loads(dic)
print(l_new, type(l_new))

print(json.dumps(True), type(json.dumps(True)))

print(str(True))

# ----------------------------------

# n = ''
# n_new = json.loads(n)
# print(n_new, type(n_new))

print("*************")
form = {}
form["loopJson"] = '{"q": 1}'
form["loopJson"] = ''
a = json.loads(form.get("loopJson")) if form.get("loopJson") else ""
print(a)
