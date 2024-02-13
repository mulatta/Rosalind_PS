def countDNA(seq):
    baseCount = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for base in seq:
        baseCount[base] += 1
    return baseCount

if __name__ == '__main__':
    path = "./rosalind_ini.txt"
    with open(path, 'r') as f:
        seq = f.readline().strip() 
        
        for count in countDNA(seq).values():
            print(count, end=' ')