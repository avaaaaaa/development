# finds all prime numbers from 2 to n(inclusive)
def prime_finder(n=0):
    try:
        n = int(n)
    except ValueError:
        return []

    if n <= 1:
        return []

    primes = [2]
    for i in range(2, n+1):
        is_prime = True
        for prime in primes:
            if i % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)

    return primes

print(prime_finder("a"))
print(prime_finder())
print(prime_finder(3))
print(prime_finder(20))
print(prime_finder(23))