# 获取系统上的CPU数量
# import multiprocessing

import psutil

# print("物理CPU：", multiprocessing.cpu_count())
print("物理CPU数量：", psutil.cpu_count())
print("逻辑CPU数量：", psutil.cpu_count(logical=False))
# print("内存：(字节)", psutil.virtual_memory())
# 1G=1024M=1024^2Kb=1024^3bytes=1024^4bit
all_info = psutil.virtual_memory()
print(f"系统总内存大小：{round((all_info.total / 1024 ** 3), 2)}G")
print(f"系统已用内存大小：{round((all_info.used / 1024 ** 3), 2)}G")
print(f"系统可用内存大小：{round((all_info.free / 1024 ** 3), 2)}G")
# pyinstaller.exe --icon="pic.ico" -F get_cpu.py 与dist目录下生成.exe可执行文件
input()

print("------------------------")

print()