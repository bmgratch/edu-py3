def proteins(strand):
    # init definitions
    protein = []
    dictRNA = {
        'AUG': "Methionine",
        'UUU': "Phenylalanine",
        'UUC': "Phenylalanine",
        'UUA': "Leucine",
        'UUG': "Leucine",
        'UCU': "Serine",
        'UCC': 'Serine',
        'UCA': 'Serine',
        'UCG': 'Serine',
        'UAU': 'Tyrosine',
        'UAC': 'Tyrosine',
        'UGU': "Cysteine",
        'UGC': "Cysteine",
        'UGG': 'Tryptophan'
        }
    codon = ''
    pro = ''

    for p in strand:
        codon += p

        if len(codon) < 3:
            pass
        elif len(codon) == 3:
            # dictRNA logic

            pro = dictRNA.get(codon, None)
            if pro != None:
                protein.append(pro)
                codon = ''
            else:
                break
    return(protein)
