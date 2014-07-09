import time
# This brute force approach takes around 18 seconds on my computer
# Could cache values for collatz sequences that were already generated
# (each time you generate the next value of the collatz sequence,
# check if it is less than 1,000,000. If so, then see if the length of the
# collatz sequence starting with that value has already been calculated etc.)
# Or could achieve even more speed up by doing the same brute force approach in C
def collatz(n):
    l = 0
    while n != 1:
        l += 1
        if not n % 2:
            n /= 2
        else:
            n = 3*n + 1
    return l + 1
start = time.time()
maxC = 1
maxN = 2
for n in range(2, 1000000):
    a = collatz(n)
    if a > maxC:
        maxC = a
        maxN = n
elapsed = time.time() - start
print "Max of %s terms for starting value %s" % (maxC, maxN)
print "%s seconds elapsed" % elapsed
