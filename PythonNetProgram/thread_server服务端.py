import socketserver
import time


ip_port = ('127.0.0.1',8080)
buffer_size = 1024
class Myserver(socketserver.BaseRequestHandler):


    def handle(self):
         conn = self.request
        addr = self.client_address
        print('conn is:', conn)
        print('addr is:', addr)

        while True:
            print('服务端等待输入')
            try:
                data = conn.recv(buffer_size)
                if not data:
                    break
                print('收到的消息:', data.decode('utf8'))
                conn.sendall(data.title())
            except expression as e:
                print(e)


if __name__ == "__main__":
    while True:
        print('服务端正在运行')
        s = socketserver.ThreadingTCPServer(ip_port, Myserver)
        s.serve_forever()
