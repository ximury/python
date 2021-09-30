import ast

ip_port = {}
ip_port["['1.1.1.1', 'view_only']"] = '6080'
# ip_port = {"['1.1.1.1', 'view_only']": '6080', "['1.1.1.1', 'control']": '6081', "['1.1.1.2', 'view_only']": '6082'}
if ip_port.get("['1.1.1.2', 'view_only']") is None and ip_port.get("['1.1.1.2', 'control']") is None:
    ip_port["['1.1.1.2', 'view_only']"] = '6082'
    ip_port["['1.1.1.2', 'control']"] = '6083'

print(ip_port)
key1 = "['1.1.1.1', 'view_only']"
if key1 in ip_port.keys():
    print(ip_port.get(key1))

"""
远程连接使用：5901
无感查看使用：5902
断开一个远程连接，如果vnc服务端没有其他vnc客户端连接，可以终止掉进程
如果还有其他vnc客户端连接，不能终止掉vnc服务端以及客户端进程，不需要给python服务端发送断开连接信号，
前端断开连接，但是不调用断开连接的逻辑
"""
"""
若远程连接与无感查看不使用同一个客户端端口，无感查看与远程连接断开互不影响，但会减少可远程连接的数量
以下不成立，因为必然需要一个新的端口！
若远程连接与无感查看使用同一个客户端端口，当一个web端打开一个远程连接再打开无感查看，会覆盖原窗口

当断开远程连接时，需要检测是否还有远程连接或者无感查看中的机器

远程连接：断开连接时，停止录制视频，
无感查看：断开连接时，不停止录制视频

客户端主动断开，只能断开远程连接，不能断开无感查看
"""

ip_port = {}
ip_port["['1.1.1.1', 'view_only']"] = '6080'
ip_port["['1.1.1.1', 'control']"] = '6080'
ip_port["['2.2.2.2', 'view_only']"] = '6081'
print(ip_port)
for server_ip in ip_port:
    real_ip = list(ast.literal_eval(server_ip))[0]
    print(real_ip)
if "['2.2.2.2', 'view_only']" in ip_port:
    print('true----')

port_num = {'6080':1, '6081':2}
if port_num.get('6083') is not None:
    port_num['6083'] = 0
print(port_num)
print(port_num.keys())
if '6081' in port_num:
    print('*****')
    del port_num['6081']
print(port_num)