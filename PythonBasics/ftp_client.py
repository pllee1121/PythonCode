'''
    反射的简单应用
'''


class FtpClient:

    def __init__(self, addr):
        self.addr = addr
        print('想要连接的服务器地址是{}'.format(self.addr))

    def put(self):
        print('正在上传文件')
