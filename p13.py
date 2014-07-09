# Python handles large integers for you.
# Otherwise, I would have to turn the integers into arrays
f = open('p13.txt','r').read().splitlines()
sumT = sum(int(n) for n in f)
sumT = str(sumT)
print sumT[:10]
