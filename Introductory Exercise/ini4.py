path = "rosalind_ini4.txt"
fileBuffer = open(path, 'r')
line = fileBuffer.readline().strip()

variables = line.strip().split()

a = int(variables[0])
b = int(variables[1])
result = 0

for i in range(a, b):
    if i % 2 == 1:
        result += i

print(result)