# Making a function that returns all the prime factors so I can use this later 
# in problem 5 (keeping number of occurences because why not)
def prime_factors(n):
    i = 2
    factors = {} # Dictionary of how many time each prime factor occurs
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            if i in factors:
                factors[i] += 1
            else:
                factors[i] = 1
    if n > 1:
        if n in factors:
            factors[n] += 1
        else:
            factors[n] = 1
    return factors
n = 600851475143
n = 20
a = prime_factors(n)
print max(a)


