
import random
a=random.randint(1, 10)
try:
    b=int(input("请您输入1--10之间的整数:")) and 1<=b<=10
    if a == b:
        print("猜对了!计算机给出的数字也是%d" % a)
    elif a > b:
        print("猜小了!计算机给出的数字是%d" % a)
    else:
        print("猜大了!计算机给出的数字是%d" % a)
except:
    print("输入错误，请输入1--10之间的整数!")
