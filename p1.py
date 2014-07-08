#Obvious method with more iterations and checks
sumT = 0
for i in range(3,1000):
    if i%3 == 0 or i%5 == 0:
        sumT += i
print sumT

#Slightly more thought (and more memory usage)
from sets import Set
x = 3
y = 5
setT = Set([])
sumT = 0
for mult in range(1,200): # 5*200 = 1000. 200 is the bound on the multiple of 5.
    setT.add(y*mult)
for mult in range(1,334): # 3*333 = 999.
    setT.add(x*mult)
print sum(setT)
    

    

    
