# data = open("datals.txt").read()
# ls = data.split(",")
# print(ls)
# data.close()

ls = ["中国","美国","日本"]
f = open('fname',"w")
f.write('$'.join(ls))
f.close()