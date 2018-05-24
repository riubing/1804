'''
key = {"name":"laowang","age":33,"sex":"nan","shengao":180,"tizhong":"60kg"}
print(key)
print(key.values())
for i in key.values():
    print(i)
'''
list = [{"上海":{"面积":"100平米","人口":"200W"},"北京":{"面积":"70平米","人口":"150W"},"南京":{"面积":"300平米","人口":"999W"}}]
for i in list:
    for d,f,g in i.items():
        for k,l,c in f.items():
            for t,u,p in c.items():
                print(d,k,l,t)










