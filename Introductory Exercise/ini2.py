path = "rosalind_ini3.txt"
fileBuffer = open(path, 'r')
lines = fileBuffer.readlines()

str = lines[0].strip()
variables = lines[1].strip().split()

a = int(variables[0])
b = int(variables[1])
c = int(variables[2])
d = int(variables[3])

print(str[a:b+1], str[c:d+1])