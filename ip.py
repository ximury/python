import re
import socket
from urllib.parse import urlparse


def get_host_ip():
    """
    查询本机ip地址
    :return:
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


def sub_ip(url):
    mode = re.compile(r'(?<![.\d])(?:\d{1,3}\.){3}\d{1,3}(?![.\d])')
    # url = 'http://www.baidu.com:80'
    ip = mode.findall(url)
    print(ip)
    if not ip:
        arr = url.split("/")
        print(arr)
        ip.append(arr[2])
    return ip[0]


def get_ip(url):
    # url = 'http://www.baidu.com:80'
    _url = urlparse(url)
    hostname = _url.hostname
    port = _url.port
    scheme = _url.scheme

    print(f'主机名:{hostname}\n端口:{port}\n协议:{scheme}')


if __name__ == '__main__':
    # print(get_host_ip(), type(get_host_ip()))
    print(sub_ip('http://172.17.4.68:5000/#/region-centre/region-detail'))
    print(get_ip('http://172.17.4.68:5000/#/region-centre/region-detail'))
