import sys, socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
print(host)
port = 1121

s.connect((host,port))

msg = s.recv(1024)
s.close()
print(msg.decode('utf-8'))