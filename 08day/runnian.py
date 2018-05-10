ddd = int(input("请输入年份 "))

if ddd%4== 0 and ddd%100 !=0:
    print("这是闰年")
elif ddd%400== 0:
    print("这也是闰年")
else:
    print("这是平年")
