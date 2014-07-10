from operator import mul
import time
start = time.time()
with open('p11grid.txt') as f:
    a = f.read().splitlines()
gSize = int(a[0])
# Get the numbers from the text file, make them integers
g = []
for i in range(1, gSize + 1):
    data = a[i].split()
    g.append([int(d) for d in data])
maxProd = 0
for i in range(20):
    for j in range(16):
        # Horizontal product
        a = reduce(mul,[g[i][x] for x in range(j,j+4)])
        if a > maxProd:
            maxProd = a
        # Vertical product
        a = reduce(mul,[g[x][i] for x in range(j,j+4)])
        if a > maxProd:
            maxProd = a
# Left Diagonal
for i in range(16):
    for j in range(3,20):
        a = g[i+3][j-3]*g[i+2][j-2]*g[i+1][j-1]*g[i][j]
        if a > maxProd:
            maxProd = a
# Right Diagonal
for i in range(16):
    for j in range(16):
        a = g[i][j]*g[i+1][j+1]*g[i+2][j+2]*g[i+3][j+3]
        if a > maxProd:
            maxProd = a
elapsed = time.time() - start
print maxProd
print "%s seconds elapsed" % elapsed
