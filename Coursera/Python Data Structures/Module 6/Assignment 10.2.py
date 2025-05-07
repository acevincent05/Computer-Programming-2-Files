name = input("Enter file:")
f = open(name)
dic = {}
for i in f:
    if i.startswith("From") and len(i.split()) > 2:
        line = i.split()
        if not dic.has_key(line[5][:2]):
            dic[line[5][:2]] = 1
        else:
            dic[line[5][:2]] += 1
                
key = sorted(dic)
for i in key:
    print (i, dic[i])