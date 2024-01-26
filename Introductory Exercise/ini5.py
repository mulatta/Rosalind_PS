path = "rosalind_ini5.txt"
fileBuffer = open(path, 'r')
lines = fileBuffer.readlines()

for i in range(len(lines)):
    if i % 2 == 1:
        print(lines[i].strip())