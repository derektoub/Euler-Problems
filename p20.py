# Again, big numbers are no problem in python
def factorial(n):
    product = 1
    if n == 1:
        return 1
    else: return n*factorial(n-1)
a = factorial(100)
greg = str(a)
sumT = sum(int(i) for i in greg)
print sumT
