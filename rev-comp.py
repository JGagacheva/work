#create a column with the reverse complement of a sequencence in a csv file
alt_map = {'ins':'0'}
complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

def reverse_complement(seq):
    for k,v in alt_map.items():
        seq = seq.replace(k,v)
    bases = list(seq)
    bases = reversed([complement.get(base,base) for base in bases])
    bases = ''.join(bases)
    for k,v in alt_map.items():
        bases = bases.replace(v,k)
    return bases

# seq = "CGCCAT"
# print(reverse_complement(seq))


import pandas as pd

#file = input("What is the name of you csv file (omit the .csv part of the name)? ")
#bcs = pd.read_csv(file + '.csv')

bcs = pd.read_csv("/Users/jana/Box/Gagacheva/Sudoku/miniseq-10-02-20/i5-barcodes.csv")

for i, row in enumerate(bcs["i5"]):
    row2 = str(row)
    #print(row2)
    rev_comp = reverse_complement(row2)
    indx = i
    bcs.at[indx, "rev_compl_i5s"] = rev_comp

bcs.to_csv("/Users/jana/Box/Gagacheva/Sudoku/miniseq-10-02-20/i5-bcs-RevComps.csv")
