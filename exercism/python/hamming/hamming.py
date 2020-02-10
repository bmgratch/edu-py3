def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands do not match lengths.')
    hamming = 0
    for dna in range(0, len(strand_a)):
        if strand_a[dna] != strand_b[dna]:
            hamming += 1
    return hamming
