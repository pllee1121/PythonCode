# import socket

# ip_port = ('127.0.0.1', 8080)
# buffer_size = 1024

# phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# phone.connect(ip_port)
# phone.send('hello'.encode('utf-8'))
# data = phone.recv(buffer_size)
# print('收到服务器端发来的消息', data.decode('utf-8'))


from socket import *

ip_port=('127.0.0.1',8080)
buffer_size=1024

client = socket(AF_INET,SOCK_STREAM)
client.connect(ip_port)

while True:
    msg = input('输入信息:').strip()
    if not msg:
        continue
    client.send(msg.encode('utf8'))
    info = client.recv(buffer_size)
    print('来自服务端的消息',info.decode('utf8'))

client.close()


