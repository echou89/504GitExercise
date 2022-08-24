def count_nts(seq):
    '''
    Returns a dictionary of counts of nucleotides.
    Params:
        seq: a sequence of nucleotides, or any string really.
    '''
    counts = dict()
    for nt in seq:
        if nt not in counts:
            counts[nt] = 1
        else:
            counts[nt] += 1
    return counts

def calc_freq(counts):
    '''
    Calculates and displays to std out the frequencies of the characters/
    nucleotides in the given sequence.
    Params:
        counts: dictionary of counts of characters.
    '''
    print('freqs')
    total = float(sum([counts[nt] for nt in counts.keys()]))
    for nt in counts.keys():
        print(nt + ':' + str(counts[nt]/total))

calc_freq(count_nts('ATCTGACGCGCGCCGC'))
