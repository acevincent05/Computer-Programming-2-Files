fname = input("Enter file name: ")
fh = open(fname)

list = []
lines = [line.split() for line in fh]

for i in lines:
    for j in i:
        if j not in list:
            list.append(j)

list.sort()
print(list)