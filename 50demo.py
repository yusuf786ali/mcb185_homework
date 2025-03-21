import random
import sys
import time
'''
random.seed(1)

names = []
vals = []
name2val = {}
with open(sys.argv[1]) as fp:
    for line in fp:
        name, val = line.split()
        name2val[name] = val
        
t0 = time.time()
names = list(name2val.keys())
for i in range(100):
    token = random.choice(names)
    print(token, name2val[token])
    #pos = names.index(token)
    #val = vals[pos]
    #print(token, pos, val)
t1 = time.time()
print(t1-t0)

"""
if 'LKHLELKKD' in names:
    pos = names.index('LKHLELKKD')
    print(vals[pos])

for i in range(100000):
    name = random.choices('ABCDEFGHIJKLMNOP', k=9)
    name = ''.join(name)
    val = random.random()
    print(name, val)
"""
'''
s = {'A', 'C', 'G'}
print(s)

s.add('T')
print(s)

s.add('A')
print(s)

d = {}
d = dict()

d = {'dog':'woof', 'cat': 'meow'}
print(d)

print(d['cat'])

d['pig'] = 'oink'
print(d)

d['cat'] = 'mew'
print(d)

del d['cat']
print(d)

if 'dog' in d: print(d['dog'])

for key in d: print(f'{key} says {d[key]}')

for k, v in d.items(): print(k, 'says', v)

for thing in d.items(): print(thing[0], thing[1])

print(d.keys(), d.values(), list(d.values()))

kdtable = {
    'I':  4.5, 'V':  4.2, 'L':  3.8, 'F':  2.8, 'C':  2.5, 'M': 1.9, 'A': 1.8,
    'G': -0.4, 'T': -0.7, 'S': -0.8, 'W': -0.9, 'Y': -1.3, 'P':-1.6, 'H': -3.2,
    'E': -3.5, 'Q': -3.5, 'D': -3.5, 'N': -3.5, 'K': -3.9, 'R': -4.5
}

def kd_dict(seq):
    kd = 0
    for aa in seq: kd += kdtable[aa]
    return kd/len(seq)