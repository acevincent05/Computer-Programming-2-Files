import re

f = open('regex_sum_2198748.txt')

f = f.read()

y = re.findall('[0-9]+', f)

print(y)