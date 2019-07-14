# import threading

# lockA = threading.Lock()
# lockB = threading.Lock()

# def printNumber(n):
    
#     if n > 50:
#         return
#     n += 1
#     lockA.acquire()
#     print("{}{}".format(n, n+1), end="")
#     lockB.release()
#     printNumber(n+1)

# def printAlpha(n):

#     if n > 90:
#         return
#     lockB.acquire()
#     print("{}".format(chr(n)), end=" ")
#     lockA.release()
#     printAlpha(n+1)

# lockB.acquire()
# t1 = threading.Thread(target = printNumber, args = (0,))
# t2 = threading.Thread(target = printAlpha, args = (65,))
# t1.start()
# t2.start()
    


# listinfo = [133, 88, 24, 33, 232, 44, 11, 44]
# listAfter = []
# def func(list_info):
#     try:
#         for l in list_info:
#             if l <= 100 and l%2 == 0:
#                 listAfter.append(l)
#         print(listAfter)
#     except:
#         print("error")

# func(listinfo)


class MyException(Exception):
    def __init__(self, message):
        Exception.__init__(self)
        self.message = message

str = input("please input string: ")

if len(str) < 12:
    try:
        raise MyException('yes')
    except MyException as e:
        print(e.message)

else:
    print('no')






















