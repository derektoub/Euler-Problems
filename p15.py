from math import factorial
# Using combinatorics, we find that an nxn grid has (2n)!/(n!)^2 paths
# Else, write a recursive function that finds all the paths and sum the number of # paths
n = 20
numPaths = int(factorial(2*n)/float(factorial(n)**2))
print numPaths
