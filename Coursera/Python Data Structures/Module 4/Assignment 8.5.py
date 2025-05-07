fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    if line.startswith("From "):
        read = line.rstrip().split()
        email = read[1]
        print(email)
        count +=1
    else:
        continue

print("There were", count, "lines in the file with From as the first word")