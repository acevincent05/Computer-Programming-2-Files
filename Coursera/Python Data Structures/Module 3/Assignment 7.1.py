# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

for line in fname:
    line = line.rstrip()

inp = fh.read()

print(inp.upper())