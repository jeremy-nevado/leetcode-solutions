class Solution:
    def countPrimes(self, n):
        if n == 0 or n == 1 or n == 2:
            return 0
        primes = [2]
        for i in range(2, n):
            isPrime = True
            for prime in primes:
                if i % prime == 0:
                    isPrime = False
                    break
            if isPrime:
                primes.append(i)
        return len(primes)
