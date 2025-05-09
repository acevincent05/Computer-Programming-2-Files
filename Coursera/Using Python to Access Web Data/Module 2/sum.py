import re

f = open('regex_sum_2198748.txt')

f = f.read()

y = re.findall('[0-9]+', f)

print(y)

sum_list = []

for i in y:
    i = int(i)
    sum_list.append(i)

print()

print(sum(sum_list))