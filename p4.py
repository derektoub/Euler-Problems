import time
start = time.time()
maxT = 0
for x in range(100, 1000):
    for y in range(100,1000):
        a = x*y
        b = str(a)
        if b == b[::-1] and a > maxT:
            maxT = a
elapsed = time.time() - start
print maxT
print "%s seconds elapsed" % elapsed
