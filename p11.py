# Assuming a square grid
from numpy import array
searchSize = 4
with open('p11grid.txt') as f:
    a = f.read().splitlines()
    gSize = int(a[0])
    # Pad the grid with zeros because I don't feel like dealing with edge cases
    grid = [0]*(gSize + searchSize - 1)
    grid = [grid]*(gSize + searchSize - 1)
    print grid[0], len(grid[0])
    # Get the numbers from the text file, make them integers
    g = []
    for i in range(1, gSize + 1):
        data = a[i].split()
        g.append(int(data))
    g = for x in 
    for l in range(0, gSize):
        grid[l + searchSize - 1][searchSize - 1:gSize] = list(g[l])
print grid
print g
