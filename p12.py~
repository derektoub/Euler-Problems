import time
def numFactors(n):
    return sum(2 for i in range(1, int(n**(0.5)+1)) if not n % i)
def triangNum(n):
    return sum(i for i in range(1, n + 1))
start = time.time()
n = 7
while numFactors(triangNum(n)) < 500:
    n += 1
elapsed = time.time() - start
print triangNum(n)
print "%s seconds elapsed" % elapsed
