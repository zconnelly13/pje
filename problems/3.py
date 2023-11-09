"""
The prime factors of 13195 are 5, 7, 13, and 29.
What is the largest prime factor of the number 600851475143?
"""


# I know this is inefficient for this particular problem but I think
# the prime sieve will be useful in future problems.


from math import sqrt, ceil


def prime_sieve(upper_bound):
    sieve = [True] * upper_bound
    sieve[0] = False
    sieve[1] = False
    i = 2
    while i < len(sieve):
        p = i
        j = 2
        while p*j < len(sieve):
            sieve[p*j] = False
            j += 1
        i += 1
    return sieve


def primes(upper_bound):
    sieve = prime_sieve(upper_bound)
    return [i for i in range(upper_bound) if sieve[i]]


def largest_prime_factor(n):
    suspects = primes(ceil(sqrt(n)))
    for s in suspects[::-1]:
        if n % s == 0:
            return s


print(largest_prime_factor(600851475143))
