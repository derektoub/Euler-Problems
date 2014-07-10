import time
# Sums from bottom are same as sums from top
# Do partial sums from second to last row, get largest sum when you reach the top.
def largestSum(tri, rowIndex):
    for i, val in enumerate(tri[rowIndex]):
        tri[rowIndex][i] += max([tri[rowIndex + 1][i], tri[rowIndex + 1][i + 1]])
    if rowIndex == 0:
        return tri[rowIndex][0]
    else:
        return largestSum(tri, rowIndex - 1)
start = time.time()
triang = []
with open('p18.txt') as f:
    d = f.read().splitlines()
    for line in d:
        triang.append([int(i) for i in line.split()])
l = largestSum(triang, len(triang) - 2)
elapsed = time.time() - start
print l
print "%s seconds elapsed" % elapsed
  

        
