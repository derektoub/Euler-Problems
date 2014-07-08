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

numPrime = 1 # Start with the prime number 2
x = 3 # Iterate through numbers starting at 3
while numPrime < 10001:
    if isPrime(x):
        numPrime += 1
    x += 2  # Only cycle through odd numbers
print x - 2
