def factors(value):
    primes = []
    for i in range(2, value+1):
        if value == 1:
            break
        while value%i == 0:
            primes.append(i)
            value = value/i
    return primes
