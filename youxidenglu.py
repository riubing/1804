print("="*30)
print( )
print("我英俊潇洒的主人")
print("欢迎来到王者荣耀注册系统")
print("祝您玩的开心")
print( )
print("="*30)
list = []
def shuru():
    sss = input("请输入注册账号")
    pwd = input("请输入注册密码")
    #判断账号存不存在
    flag = 0
    for i in list:
        if sss == i["sss"]:
            print("此账号已存在,请重新注册")
            flag = 1
            break
    if flag == 0:
        dict = {}
        dict["sss"] = sss
        dict["pwd"] = pwd
        list.append(dict)
        print("注册成功")
def denglu():
    sss = input("请输入账号")
    pwd = input("请输入密码")
    flag = 0
    for i in list:
        if sss == i["sss"]:
            if i.get("status") == 1:
                print("账号已登录")
            else:
                if pwd == i["pwd"]:
                    print("登录成功")
                    i["status"] = 1
                else:
                    print("密码错误,登录失败")
            flag = 1
            break
    if flag == 0:
        print("账号不存在，请先注册")
def dengchu():
    sss = input("请输入账号")
    pwd = input("请输入密码")
    flag = 0
    for i in list:
        if sss == i["sss"]:
            if i.get("status") == 1:
                print("退出成功")
                i.get("status") == 0
            else:
                print("账号未登录")
                flag == 1
                break
                #flag == 0
                #print("账号不存在")

#def shanchu():
    #sss=input("请输入要删除的账号")
    #pwd=input("请输入要删除账号的密码")
    #sss=



while True:
    cux = int(input("请选择功能：1:注册账号2:登录游戏3:删除账号4:修改账号:"))
    if cux == 1:
                shuru()
    elif cux == 2:
                denglu()
    elif cux == 3:
                shanchu()
    elif cux == 4:
                xiugai()
