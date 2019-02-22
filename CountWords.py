from collections import Counter

# Reading file 
f = open('data.txt','r')
data = f.read()

c = Counter()
for line in data.splitlines():
    c.update(line.split())
print(c)