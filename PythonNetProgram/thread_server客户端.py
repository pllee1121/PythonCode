from socket import *

ip_port=('127.0.0.1',8080)
client = socket(AF_INET,SOCK_STREAM)
client.connect(ip_port)

while True:
    scan = input("请输入:")
    if scan=='quit':
        break
    if not scan:
        continue
    client.send(scan.encode('utf8'))
    data = client.recv(1024)
    print('服务端发来的消息',data.decode('utf8'))