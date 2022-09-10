# dumps功能
import pickle

data = ['aa', 'bb', 'cc']
# dumps 将数据通过特殊的形式转换为只有python语言认识的字符串
p_str = pickle.dumps(data)
print(p_str)

# loads功能
# loads  将pickle数据转换为python的数据结构
ret = pickle.loads(p_str)
print(ret)

"""
# dump功能
# dump 将数据通过特殊的形式转换为只有python语言认识的字符串，并写入文件
with open('data.pkl', 'wb') as f:
    pickle.dump(data, f)
print("*******")
# load功能
# load 从数据文件中读取数据，并转换为python的数据结构
with open('data.pkl', 'rb') as f:
    data = pickle.load(f)
"""