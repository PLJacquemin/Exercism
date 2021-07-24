def primes(limit):
    sieve_range = range(2,limit+1)
    marked = []
    primes_list = []
    for i in sieve_range:
        if i not in marked:
            primes_list.append(i)
            for j in sieve_range:
                if i*j > limit:
                    break
                elif i*j not in marked:
                    marked.append(i*j)
    return primes_list
