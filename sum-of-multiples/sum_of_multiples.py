def sum_of_multiples(limit, multiples):
    numbers = []
    for mul in multiples:
        n = 1
        if mul == 0:
            continue
        while mul*n < limit:
            numbers.append(mul*n)
            n += 1
    return sum(set(numbers))
