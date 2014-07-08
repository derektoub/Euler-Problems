def squareOfSum(n):
    sumT = n*(n+1)/2
    sumT *= sumT
    return sumT

def sumOfSquares(n):
    sumS = 0
    for i in range(1,n+1):
        sumS += i*i
    return sumS

n = 100
sqos = squareOfSum(n)
sosq = sumOfSquares(n)
print sqos - sosq
