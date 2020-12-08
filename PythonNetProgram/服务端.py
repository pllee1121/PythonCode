# import socket

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(('127.0.0.1', 8080))
# server.listen(5)
# conn, addr = server.accept()
# msg = conn.recv(1024)
# print('客户端发来的消息',msg.decode('utf-8'))
# server.send('goodbye'.encode('utf-8'))

# conn.close()
# server.close()


from socket import *

ip_port = ('127.0.0.1', 8080)
buffer_size = 1024

server = socket(AF_INET, SOCK_STREAM)
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 释放IP和端口
server.bind(ip_port)
server.listen(5)
while True:
    print('服务端开始运行')
    conn, addr = server.accept()
    print(conn)
    print(addr)
    while True:
        try:
            msg = conn.recv(buffer_size)
            if not msg:
                break
            print('来自客户端的信息是', msg.decode('utf8'))
            conn.send(msg.upper())
        except Exception:
            break
    conn.close()
server.close()
