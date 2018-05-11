'''
import random
while True:
#1 = "石头"
#2 = "剪刀"
#3 = "布"
user = int(input("1--石头 2--剪刀 3--布:"))
cp = random.randint(1,3)
print("他出了%d "%cp)
if (user==1 and cp==2) or (user==2 and cp==3) or (user==3 and cp==1):
    print("玩家赢")
elif user == cp:
    print("平局")
else:
    print("你太小看我了")
'''







import random
while True:
    cp = random.randint(1,3)
    user=int(input("请输入1--石头 2--剪刀 3--布:"))
#print("他出的是%d "%user)
    if cp == 1:
        print("他出了石头")
    elif cp == 2:
        print("他出了剪刀")
    elif cp == 3:
        print("他出了布")
    if (user==1 and cp==2) or (user==2 and cp==3) or (user==3 and cp==1):
        print("玩家赢")
    elif user == cp:
        print("平局")
    else:
        print("你不行")

































'''
import random
while True:
    mm = random.randint(1,3)
    llis = int(input("1==最最最  2==愿望 3==伟大抱负:"))
    if (llis==1 and mm==2) or(llis==2 and mm==1) or (llis==3 and mm==2):
        print("最最最爱刘蕊")
    elif mm == llis:
        print("一定要娶了刘蕊")
    else:
        print("一定给刘蕊一个家")
'''














