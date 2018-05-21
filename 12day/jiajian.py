p = input("欢迎使用计算机")
def jia(a,l):
    return (a+l)
def jian(a,l):
    return (a-l)
def cheng(a,l):
    return (a/l)
def chu(a,l):
    return (a*l)
while True:
    a = input("请输入一个数字")
    suss = input("请选择符号：(+ - * /)")
    if s=='q':
        break
    l = input("请输入第二个数字")
    if suss == "+":
        m = jia(a,l)
        print(m)
    elif jian== "-":
        m = jian(a,l)
        print(m)
    elif cheng == "*":
        m = cheng(a,l)
        print(m)
    elif chu == "/":
        m = chu(a,l)
        print(m)
    else:
        print("输入错误")



