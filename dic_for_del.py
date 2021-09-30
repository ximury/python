"""
login_time:唯一标志一台WEB端机器,进入组织架构的时间（保证一个web界面是唯一的）
上次请求的时间
"""
login_time_port = {}
# {[ip,port]: refresh_time}
login_time_port["1001"] = {'2100': '6080'}
login_time_port["1010"] = ['2110', '6081']
login_time_port["1003"] = ['2130', '6082']
login_time_port["1100"] = ['2135', '6082']

print(login_time_port)
del_keys = []

for key in login_time_port:
    if int(key) < 1005:
        del_keys.append(key)
        # del login_time_port[key]
print(del_keys)

for i in del_keys:
    del login_time_port[i]

print(login_time_port)

print(login_time_port.get('1100')[0])


print('999999999999999999999999999999999999999999')


ip_port = {"['172.17.129.220', 'control']": '6080', "['172.17.129.221', 'control']": '6081'}
print(ip_port.keys())
key = "['{}', 'control']".format('172.17.129.220')
if str(key) in ip_port.keys():
    print('in')
    del ip_port[key]

print(ip_port)