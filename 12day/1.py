def jia(a,b):
    return a+b
def jian(a,b):
    return (a-b)
def cheng(a,b):
    return (a*b)
def chu(a,b):
    return (a/b)
a = int(input ('输入第一个数字：'))
fuhao = input("请输入要做的运算符号：(+ - * /)")
b = int(input ('输入第二个数字：'))
if fuhao == "+":
    s = jia(a,b)
    print (s)
