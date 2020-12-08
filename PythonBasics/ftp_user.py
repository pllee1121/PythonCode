'''
    反射的简单应用
'''

from ftp_client import FtpClient

f1 = FtpClient('192.168.2.1')
if hasattr(f1, 'put'):
    func_get = getattr(f1, 'put')
    func_get()
else:
    print('put方法不存在')
