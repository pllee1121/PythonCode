from socket import *

ip_port = ('127.0.0.1', 8080)
buffer_size=1024
udp_client = socket(AF_INET, SOCK_DGRAM)
while True:
    msg = input('请输入要发送的信息: ')
    udp_client.sendto(msg.encode('utf8'), ip_port)
    data, addr= udp_client.recvfrom(buffer_size)
    print('接收来自服务器的信息:',data.decode('utf8'))