positive_numbers = []
minuses = []
zeros = []

print("请每行输入一个数: ")
for i in range(10):
    number = eval(input())
    if number == 0:
        zeros.append(number)
    elif number > 0:
        positive_numbers.append(number)
    else:
        minuses.append(number)

 
def fun(numbers_list):
    numbers_sum = 0
    for number_list in numbers_list:
        numbers_sum += number_list
    return numbers_sum

positive_sum = fun(positive_numbers)
minuses_sum = fun(minuses)
zeros_length = len(zeros)

print("正数之和为" + str(positive_sum))
print("负数之和为" + str(minuses_sum))
print("共有" + str(zeros_length) + "个零")