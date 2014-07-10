import time
start = time.time()
ones = {0:0,1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4}
tens = {0:0,2:6,3:6,4:5,5:5,6:5,7:7,8:6,9:6}
hundreds = {1:10,2:10,3:12,4:11,5:11,6:10,7:12,8:12,9:11}
oneInTens = {0:3,1:6,2:6,3:8,4:8,5:7,6:7,7:9,8:8,9:8}
l = 0
for x in range(1,1000):
    o = x % 10 # ones digit
    t = ((x % 100) - o) / 10 # tens digit
    h = ((x % 1000) - (t * 10) - o) / 100 # hundreds digit    
    if h:
        l += hundreds[h]
        if t or o:
            l += 3 # Account for addition of "and"
    if t == 1:
        l += oneInTens[o]
    else:
        l += tens[t] + ones[o]
elapsed = time.time() - start
print l + 11
print "%s seconds elapsed" % elapsed
#1000 has 11 letters, and I just add this at the end
