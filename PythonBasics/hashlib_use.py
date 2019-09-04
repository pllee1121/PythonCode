'''
    hash 算法对文本进行加密
'''

import hashlib

h = hashlib.md5()              # 加入参数 h = hashlib.md5('hash'.encode('utf8'))
h.update('admin'.encode('utf8'))
print(h.hexdigest())  # 21232f297a57a5a743894a0e4a801fc3

h.update('root'.encode('utf8'))  # 此步操作相当于 h.update('adminroot'.encode('utf8'))
print(h.hexdigest())  # 4b3626865dc6d5cfe1c60b855e68634a


h1 = hashlib.sha256()
h.update('admin'.encode('utf8'))
print(h.hexdigest())