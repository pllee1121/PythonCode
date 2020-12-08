'''
    导入dynamic.dynamic_import_module了模块
    但是只是获取到了 dynamic
 '''
# d = __import__('dynamic.dynamic_import_module')
# print(d)
# d.dynamic_import_module.test1()

import importlib

i = importlib.import_module('dynamic.dynamic_import_module')
print(i)
i.test1()