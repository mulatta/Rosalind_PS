from pprint import pprint as pp
path = "rosalind_ini6.txt"
fileBuffer = open(path, 'r')

text = fileBuffer.readline()
words = text.strip().split()
result = {}

for word in words:
    result[word] = 0 

for word in words:
    result[word] += 1

for key, value in result.items():
    print(key, value)