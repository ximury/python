import socket

import time

ip_port = {'1': '111', '2': '222', '3': '333'}
server_ip = '192.168.17.5'
time1 = time.time()
print(time1)
while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    time2 = time.time()
    if time2 - time1 > 10:
        break
    time.sleep(1)
    print(ip_port)
    for ip in ip_port:
        try:
            status = s.connect_ex((server_ip, 5901))
            print('ip:', ip)
            if ip_port.get('2') == '222':
                del ip_port['2']
                # break 避免 dictionary changed size during iteration
                break
        except Exception as e:
            print(e)
