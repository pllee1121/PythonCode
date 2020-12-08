#-*- coding:utf-8 -*-
from socket import *

ip_port = ('127.0.0.1', 8080)
buffer_size = 1024

udp_server = socket(AF_INET, SOCK_DGRAM)
udp_server.bind(ip_port)
print('服务器开始运行')
while True:
    msg, addr= udp_server.recvfrom(buffer_size)
    print('来自upd客户端的信息',msg.decode('utf8'))
    udp_server.sendto(msg.upper(),addr)

udp_server.close()