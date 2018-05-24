'''
import time
for i in range(1,1001):
    print(i)
    time.sleep(0.02)
'''
c = lambda d,l : d*l
print(c(3,5))
l = lambda t,p,v : t*p-v
print(l(3,6,11))
j = lambda h,g,f,s : h*g/f+s
print(j(99,34,25,1))
l = [(lambda a**2),(lambda l**4)]
