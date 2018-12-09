from pymysql import *
def join():
    print('/////////////////////////////////////////////////////////////')
    # 与数据库建立连接,Connection对象
    conn = connect(host='localhost', port=3306, database='xm', user='root', password='ruibing99', charset='utf8')
    # 获得Cursor对象
    csl = conn.cursor()
    return conn,csl
def login():
    username = input('请输入用户名: ')
    passwd = input('请输入密码: ')
    conn,csl = join()
    a = csl.execute('select * from login')
    for i in range(a):
        #获取查询到的结果
        result = csl.fetchone()
        if username == result[0] and passwd == result[1]:
            print('登录成功')
            print("欢迎%s顾客进入本店".center(50,"=")%username)
            print("1.添加")
            print("2.修改")
            print("3.删除")
            print("4.退出")
            print("5.查询")
            a = int(input("请选择操作序号: "))
            if a == 1:
                insert()
            elif a == 2:
                alert()
            elif a == 3:
                delete()
            elif a == 5:
                select()
            elif a == 4:
                break
            else:
                print("输入错误")
            break
        else:
            print("没有这个用户或者密码错误")
def zhuce():
    conn,csl = join()
    a = 0
    while a == 0:
        username = input('请输入用户名: ')
        passwd = input('请输入您要保留的密码: ')
        sql = '''select username from login where username=%s'''
        jieguo = csl.execute(sql,username)
        if jieguo == 0:
            a = csl.execute('insert into login values ("{}","{}")'.format(username, passwd))
            conn.commit()
            print("注册成功")
            a = 1
        else:
            print("用户名重复,请重试")
    conn.close()
    csl.close()
def insert():
    conn,csl = join()
    name = input("请输入您的姓名: ")
    address = input("请输入您的收获地址: ")
    phone = input("请输入您的联系电话: ")
    csl.execute('insert into user values (9,"{}","{}","{}")'.format(name,address,phone))
    print("添加成功")
    conn.commit()
    conn.close()
    csl.close()
def alert():
    conn,csl = join()
    while True:
        print("1.修改姓名".center(30,'*'))
        print("2.修改收获地址".center(30,'*'))
        print("3.修改电话".center(30,'*'))
        print("4.返回".center(30,"*"))
        num = int(input("请输入选项: "))
        if num == 1:
            oldname = input("请输入您的姓名: ")
            newname = input("请输入您的新姓名: ")
            csl.execute('update user set user_name = "{}" where user_name = "{}"'.format(newname,oldname))
            print("姓名修改成功")
        elif num == 2:
            old_address = input("请输入您的姓名: ")
            new_address = input("请输入您的新地址: ")
            csl.execute('update user set address = "{}" where user_name = "{}"'.format(new_address,old_address))
            print("地址修改成功")
        elif num == 3:
            old_phone = input("请输入您的姓名: ")
            new_phone = input("请输入新的电话号码: ")
            csl.execute('update user set tel = "{}" where user_name = "{}"'.format(new_phone,old_phone))
            print("电话号码修改成功")
        elif num == 4:
            break
        else:
            print("输入错误请重试")
    conn.commit()
    conn.close()
    csl.close()
def delete():
    conn,csl = join()
    while True:
        my = input("请输入的姓名: ")
        sql = 'select user_name from user where user_name = "%s"'
        aaa = csl.execute(sql,my)
        if aaa == 1:
            csl.execute('delete from user where user_name = "{}"'.format(my))
            conn.commit()
            print("删除成功")
        else:
            print("meiyou1")
    conn.close()
    csl.close()
def select():
    conn,csl = join()
    while True:
        print("查询服务".center(30,'='))
        print("1.查看所有顾客的信息")
        print("2.查询某一顾客的信息")
        print("3.查询某一顾客的地址")
        print("4.查询某一顾客的电话")
        print("5.查看价格最贵的商品")
        print("6.查询购买商品价格最贵的顾客")
        print("0.返回")
        boot = int(input("请输入选项: "))
        if boot == 1:
            jieguo = csl.execute('SELECT * FROM `user` '
                        'JOIN dingdan ON `user`.id = dingdan.user_id '
                        'JOIN dingdan_details dd ON dingdan.id = dd.dingdan_id '
                        'JOIN goods ON dd.goos_id = goods.id '
                        'JOIN goods_cates ON goods.cate_id = goods_cates.id '
                        'JOIN goods_brands ON goods.brand_id = goods_brands.id')
            for i in range(jieguo):
                result = csl.fetchone()
                print("="*50)
                print("姓名:%s"%result[1])
                print("收获地址:%s"%result[2])
                print("联系电话:%s"%result[3])
                print("下单时间:%s"%result[5])
                print("商品类型:%s"%result[17])
                print("商品品牌:%s"%result[19])
                print("商品名称:%s"%result[12])
                print("商品数量:%s"%result[10])
                print("商品价格:%s"%result[15])
        elif boot == 2:
            while True:
                xinxi = input("请输入姓名: ")
                sql = '''select user_name from user where user_name = %s'''
                zhi = csl.execute(sql,xinxi)
                print(zhi)
                if zhi == 0:
                    print("没有此人")
                else:
                    aa = csl.execute('SELECT * FROM `user` '
                                'JOIN dingdan ON `user`.id = dingdan.user_id '
                                'JOIN dingdan_details dd ON dingdan.id = dd.dingdan_id '
                                'JOIN goods ON dd.goos_id = goods.id '
                                'JOIN goods_cates ON goods.cate_id = goods_cates.id '
                                'JOIN goods_brands ON goods.brand_id = goods_brands.id '
                                'where `user`.user_name = "{}"'.format(xinxi))
                    for i in range(aa):
                        result_xinxi = csl.fetchone()
                        print("=" * 50)
                        print("姓名:%s" % result_xinxi[1])
                        print("收获地址:%s" % result_xinxi[2])
                        print("联系电话:%s" % result_xinxi[3])
                        print("下单时间:%s" % result_xinxi[5])
                        print("商品类型:%s" % result_xinxi[17])
                        print("商品品牌:%s" % result_xinxi[19])
                        print("商品名称:%s" % result_xinxi[12])
                        print("商品数量:%s" % result_xinxi[10])
                        print("商品价格:%s" % result_xinxi[15])
                    break
        elif boot == 3:
            name2 = input("请输入姓名")
            jieguo3 = csl.execute('select address from user where user_name = "{}"'.format(name2))
            for i in range(jieguo3):
                bb = csl.fetchone()
                print(bb)
        elif boot == 4:
            name3 = input("请输入姓名")
            jieguo4 = csl.execute('select tel from user where user_name = "{}"'.format(name3))
            for i in range(jieguo4):
                bb1 = csl.fetchone()
                print(bb1)
        elif boot == 5:
            zhi4 = csl.execute('select group_concat(goods_name),max(price) from goods')
            for i in range(zhi4):
                result4 = csl.fetchone()
                print(result4)
        elif boot == 6:
            me = input("请输入姓名: ")
            jieguo5 = csl.execute('SELECT group_concat(goods_name),group_concat(user.user_name),MAX(price) '
                                  'FROM goods '
                                  'JOIN dingdan_details dd '
                                  'ON goods.id = dd.goos_id '
                                  'JOIN dingdan ON dd.dingdan_id = dingdan.id '
                                  'JOIN `user` ON dingdan.user_id = `user`.id '
                                  'WHERE user.user_name = "{}"'.format(me))
            for i in range(jieguo5):
                result5 = csl.fetchone()
                print(result5)
        elif boot == 0:
            break
        else:
            print("输入错误")
    conn.close()
    csl.close()
def main():
    while True:
        print('欢迎进入小淘宝用户管理系统'.center(50,'='))
        print('1.登录'.center(52,' '))
        print('2.注册'.center(52,' '))
        print('3.注销'.center(52,' '))
        yonghu = int(input('请输入序号选择功能: '))
        if yonghu == 1:
            login()
        elif yonghu == 2:
            zhuce()
        elif yonghu == 3:
            break
        else:
            print("输入错误")
if __name__ == '__main__':
    main()
