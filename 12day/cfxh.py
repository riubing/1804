a=input("欢迎使用计算机")
def jia(a,b):
    return a+b
def jian(a,b):
    return a-b
def cheng(a,b):
    return a*b
def chu(a,b):
    return a/b
while True:
    k=input("请输入一个数字")
    l=input("请选择符号(+,-,*,/)")
    if (s == 'q'):
        break
    d=int(input("请输入第二个数字"))
    if s=='+':
        w=jia(a,d)
        print(w)
    elif s=='-':
        w==jian(a,d)
        print(w)
    elif s=='*':
        w==cheng(a,d)
        print(w)
    elif s=='/':
        w==chu(a,d)
        print(w)
    else:
        print("输入错误")


