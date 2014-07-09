import time
# Python makes things easy again, big numbers are no problem
start = time.time()
x = str(2**1000)
x = sum(int(a) for a in x)
elapsed = time.time() - start
print "%s found in %s seconds" % (x,elapsed)
