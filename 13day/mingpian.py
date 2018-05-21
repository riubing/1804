list_lll = []
def mingpian():
    print("="*40)
    print("非常欢迎你使用名片系统")
    print("1:创建名片")
    print("2:查看名片")
    print("3:修改名片")
    print("4:退出程序")
    print("="*40)
def chuangjian():
    print("="*40)
    print("创建名片")
    name = input("请输入姓名")
    sjh = input("请输入手机号")
    jtzz = input("请输入家庭住址")
    zhiwei = input("请输入工作单位")
    dit = {'name':name,"sjh":sjh,"jtzz":jtzz,"zhiwei":zhiwei}
    list_lll.append(dit)
    print(dit)
    print("保存成功 姓名是%s "%dit["name"])
def chakan():
    list_lll = input("请输入要查看的名片姓名")






    find_flag = 0
    for j in chakan:
        if chankan == j["name"]:
            find_flag = 1
            chakan.infors.remove(j)
            print("删除成功")
            break


def tuichu():
    print("安全退出系统成功")
mingpian()
while True:
    up = int(input("请输入编号"))
    if up == 1:
        chuangjian()
    elif up == 2:
        chakan()
    elif up == 3:
        xiugai()
    else:
        tuichu()
    break

