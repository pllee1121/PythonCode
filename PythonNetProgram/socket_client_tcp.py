from socket import *

ip_port = ('127.0.0.1', 8080)
buffer_size = 1024

client = socket(AF_INET, SOCK_STREAM)
client.connect(ip_port)
while True:
    msg = input('请输入命令: ').strip()
    if not msg:
        continue
    if msg == 'quit':
        break
    client.send(msg.encode('utf-8'))
    data = client.recv(buffer_size)
    print(data.decode('utf-8'))
client.close()