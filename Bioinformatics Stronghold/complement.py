def Complement(S):
    complementSet = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    Sc = ''
    for s in S:
        Sc += complementSet.get(s)
    return Sc

def RevComp(S):
    return Complement(S)[::-1]

if __name__ == '__main__':
    path = "Rosalind_PS/Bioinformatics Stronghold/rosalind_revc.txt"
    with open(path, 'r') as f:
        S = f.readline().strip()
        
        print(RevComp(S))