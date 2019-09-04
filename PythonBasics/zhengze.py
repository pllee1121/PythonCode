import re
r = re.findall('p..ee', 'lplpllee')
s = re.findall('^l..p', 'lplplplpllee')
l = re.findall('p...e$', 'lplplplpllee')
q = re.findall('lplp*', 'plleelpl')
p = re.findall('lplp?', 'plleelpl')
o = re.findall('lplp+', 'plleelplppppp')
a = re.findall('lplp{3}', 'plleelplppppp')
# 惰性匹配 在符号后加 ? 惰性匹配的作用是实现最小的那个匹配方式
u = re.findall('lplp+？', 'plleelplppppp')
print(u)
