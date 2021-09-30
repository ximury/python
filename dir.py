import os

str = os.getcwd()
print(str)

for root, dirs, files in os.walk(str):
    # print(root) #当前目录路径
    # print(dirs) #当前路径下所有子目录
    # print(files) #当前路径下所有非目录子文件
    pass



# 递归获取目录下以及其子目录所有文件名
def listdir(path, list_name):  #传入存储的list
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
           listdir(file_path, list_name)
        else:
            list_name.append(file_path)
    print(list_name)
    return list_name

# 获取目录下所有文件(文件带路径)
def list_dir_for_file1(path, list_name):  #传入存储的list
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            pass
        else:
            list_name.append(file_path)
    print(list_name)
    return list_name

# 获取目录下所有文件(文件不带路径)
def list_dir_for_file2(path, list_name):  #传入存储的list
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            pass
        else:
            list_name.append(file)
    print(list_name)
    return list_name

if __name__ == '__main__':
    # listdir('D:\PycharmProjects\TestCode', [])
    list_dir_for_file1('D:\PycharmProjects\TestCode', [])
    list_dir_for_file2('D:\PycharmProjects\TestCode', [])
