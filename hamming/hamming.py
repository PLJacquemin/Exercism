def distance(strand_a, strand_b):
    hamming = 0
    if len(strand_a) != len(strand_b):
        raise ValueError("Check your strands")
    elif len(strand_a) == len(strand_b):
        for l in range(len(strand_a)):
            if strand_a[l] != strand_b[l]:
                hamming += 1
        return hamming
