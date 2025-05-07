fname = input("Enter file name: ")
fh = open(fname)
count = 0
s = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    pos = line.find('0')
    s += float(line[pos:pos+6])
    count += 1
    average = s / count
print("Average spam confidence:", average)