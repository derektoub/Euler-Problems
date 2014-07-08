fib1 = 1
fib2 = 2
sumT = 2
tmp = fib1
while(fib1 + fib2 < 4000000):
    if (fib1 + fib2)%2 == 0:
        sumT += fib1 + fib2
    tmp = fib1
    fib1 = fib2
    fib2 = tmp + fib2
print sumT
