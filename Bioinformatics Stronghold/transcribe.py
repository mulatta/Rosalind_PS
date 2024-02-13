# 주어진 DNA를 RNA로 변환하여 출력
# T만 U로 바꾸면 됨
def transcribe(DNA):
    RNA = ''
    for base in DNA:
        # DNA에서 나타날 수 있는 base만 모아둔 list 선언
        baseList = ['A', 'T', 'G', 'C']
        
        # 불가능한 base가 출현 시 error
        if base not in baseList:
            raise ValueError(f"Invalid base: {base}.")
        
        # DNA에서 T가 나타나면 U를 붙임
        elif base == 'T':
            RNA += 'U'
        
        # 나머지 base는 그대로 붙임
        else:
            RNA += base

    return RNA

if __name__ == '__main__':
    path = "Rosalind_PS/Bioinformatics Stronghold/rosalind_rna.txt"
    with open(path, 'r') as f:
        DNA = f.readline().strip()
        print(transcribe(DNA))
