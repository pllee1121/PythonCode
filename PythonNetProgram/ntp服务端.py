from socket import *
import time
ip_port = ('127.0.0.1', 8080)
buffer_size = 1024

udp_server = socket(AF_INET, SOCK_DGRAM)
udp_server.bind(ip_port)
print('服务器开始运行')
while True:
    return_time = time.strftime('%Y-%m-%d %X')
    data, addr = udp_server.recvfrom(buffer_size)
    udp_server.sendto(return_time.encode('utf8'), addr)

udp_server.close()
