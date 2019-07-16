f = open('output.txt','w+')
ls = ["中国","美国","法国"]
f.writelines(ls)
f.seek(0)
for line in f:
    print(line)
f.close()