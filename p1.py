import time
#Obvious method with more iterations and checks
start = time.time()
sumT = 0
for i in range(3,1000):
    if i%3 == 0 or i%5 == 0:
        sumT += i
elapsed = time.time() - start
print "Method 1: %s seconds elapsed" % elapsed
print sumT

#Slightly more thought, fewer iterations, and more memory usage
#Actually ends up taking as long or longer than Method 1
start = time.time()
x = 3
y = 5
setT = {}
sumT = 0
for mult in range(1,200): # 5*200 = 1000. 200 is the bound on the multiple of 5.
    setT.add(y*mult)
for mult in range(1,334): # 3*333 = 999.
    setT.add(x*mult)
elapsed = time.time() - start
print "Method 2: %s seconds elapsed" % elapsed
print sum(setT)
