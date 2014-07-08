def primeFacts(n):
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
n = 20
smallest = 1 # Will become smallest number divisible by 1->n after manipulation

# Find the prime factors of numbers up to n (= 20) and greatest powers
# then multiply p1**exp1 * p2**exp2 etc. to get the smallest num divis. by 1->n
finalFacts = {}
for num in range(2, n + 1):
    a = primeFacts(num)
    for fact in a:
        if fact in finalFacts:
            if a[fact] > finalFacts[fact]:
                finalFacts[fact] = a[fact]
        else:
            finalFacts[fact] = a[fact]
for fact in finalFacts:
    smallest *= fact**finalFacts[fact]
print smallest
    
    
    
