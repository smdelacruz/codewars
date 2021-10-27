def DNA_strand(dna):
    """
    Other solution in codewars
    DNA_strand ("ATTGC") # return "TAACG"
    DNA_strand ("GTAT") # return "CATA"
    """
    complements = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G',
    }
    # return ''.join([complements[c] for c in dna])
    print(''.join([complements[c] for c in dna]))

DNA_strand("ATTGC")