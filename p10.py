# Could modify isPrime since I know that 2 is the only even prime, and will
# only come up once in the search for primes under 2,000,000
def isPrime(n):
    # If less than two, or even number, definitely not prime
    if n < 2: 
         return False;
    if n % 2 == 0:
         return False
    # Test if divisible by just odd numbers to save time
    k = 3
    while k*k <= n:
         if n % k == 0:
             return False
         k += 2
    # If not divisible by anything, it is prime
    return True
sumT = 2 # Start with 2, the only even prime
x = 3
while x < 2000000:
    if isPrime(x):
        sumT += x
    x += 2
print sumT
