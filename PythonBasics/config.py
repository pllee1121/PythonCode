'''
 文件配置模块的使用
'''

import configparser

config = configparser.ConfigParser()

# 添加文件配置
# config['test'] = {1:'one',2:'two',3:'three',4:'four'}
# with open('text','w') as f:
#     config.write(f)

# 读取文件
# config.read("text.ini")
# print(config.sections())
# print(type(config['test']))
# print(config['test']['2'])

# print('-'*10)
# for key in config['test']:
#     print(key)

# # 查询信息
# print(config.options('test'))
# print(config.items('test'))
# print(config.get('test','1'))

# # 增加新的块
# config.add_section('add')
# config.write(open('text.ini','w'))
# config.set('add','info','this is configparser')
# config.write(open('text.cfg','w'))

# # 删除模块
# config.remove_section('add')
# config.write(open('text.cfg','w'))

# 删除模块中的指定元素
config.read('text.cfg')
# config.remove_option('test', '1')
config.write(open('text.cfg','w'))
