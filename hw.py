scores =[]
judges = ['A','B','C','D','E','F','G']
sum = 0
for judge in judges:
    score = eval(input("请输入评委" + judge + "给出的成绩:"))
    scores.append(score)
scores.remove(max_score)
scores.remove(min_score)
for score in scores:
    sum += score
average = sum/len(scores)
print("去掉一个最高分" + str(max_score))
print("去掉一个最低分" +str(min_score))
print("最终得分" + str(average))
