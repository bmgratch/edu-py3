def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands do not match lengths.')
    hamming = 0
    for dna in zip(strand_a, strand_b):
        if dna[0] != dna[1]:
            hamming += 1
    return hamming
