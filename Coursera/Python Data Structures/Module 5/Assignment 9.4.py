name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

dict = {}

for lines in handle:
    if lines.startswith("From "):
        words = lines.split()
        email = words[1]
        dict[email] = dict.get(email, 0)+1
                   
i = None
j = None

for k, v in dict.items():
    if j is None or j < v:
        j = v
        i = k
print(i, j)