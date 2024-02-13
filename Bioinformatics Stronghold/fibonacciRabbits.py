# generation | number of rabbits [origin rabbit] + {new offspring rabbits}
# 1 --> [1]
# 2 --> [1]
# 3 --> [1] + {(1 * 3)} = 4
# 4 --> [1] + {(1 * 3)} + [(1 * 3)] = 7
# 5 --> [1] + {(1 * 3)} + [(1 * 3)] + {(1 * 3) * 3} + [(1 * 3)] = 19
# F_n = F_n-1 + F_n-2 * 3

def fibonacciRabbits(n, k):
    if n == 1: return 1
    elif n == 2: return 1
    else:
        return fibonacciRabbits(n - 1, k) + fibonacciRabbits(n - 2, k) * k
    
def fibonacciRabbitsbyDP(n, k):
    lineage = [1, 1]
    for gen in range(2, n):
        lineage.append(lineage[gen - 1] + k * lineage[gen - 2])
    return lineage[n-1]


if __name__ == '__main__':
    path = "Rosalind_PS/Bioinformatics Stronghold/rosalind_fib.txt"
    with open(path, 'r') as f:
        n, k = map(int, f.readline().strip().split())

        print(fibonacciRabbits(n, k))
        print(fibonacciRabbitsbyDP(n, k))