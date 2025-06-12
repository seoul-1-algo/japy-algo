n = int(input())

oddNums = [1, 3, 5, 7, 9]


def amazingPrimes(n):
    if n == 1:
        return [2, 3, 5, 7]

    primes = amazingPrimes(n - 1)
    result = []
    for prime in primes:
        for odd in oddNums:
            num = int(str(prime) + str(odd))
            is_prime = True
            for i in range(2, (num + 1) // 2):
                if num % i == 0:
                    is_prime = False
            if is_prime:
                result.append(num)
    return result


answer = amazingPrimes(n)
for amazingPrime in answer:
    print(amazingPrime)
