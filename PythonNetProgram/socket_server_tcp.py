from socket import *
import subprocess

ip_port = ('127.0.0.1', 8080)
buffer_size = 1024

server = socket(AF_INET, SOCK_STREAM)
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 释放地址端口
server.bind(ip_port)
server.listen(5)
while True:
    print('服务器运行了')
    conn, addr = server.accept()
    print('客户端链接', addr)
    while True:
        try:
            cmd = conn.recv(buffer_size)
            if not cmd:
                break
            print('客户端发来的消息{}'.format(cmd.decode('utf-8')))
            res = subprocess.Popen(cmd, shell='True', stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE, stdin=subprocess.PIPE)

            err = res.stderr.read()
            if err:
                cmd_res = err
            else:
                cmd_res = res.stdout.read()
            conn.send(cmd_res)
        except Exception as e:
            print(e)
            break

    conn.close()
server.close()
