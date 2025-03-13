import sys
import gzip
import mcb185

filepath = sys.argv[1]
fp = gzip.open(filepath, 'rt')
total_len = 0
num_exons = 0
'''
for line in fp:
    cols = line.split()
    if cols[2] == 'exon':
        beg = int(cols[3])
        end = int(cols[4])
        total_len += end - beg + 1
        num_exons += 1
print(total_len/num_exons)    
'''
'''exons = 0
total = 0
with gzip.open(filepath, 'rt') as fp:
    for line in fp:
        f = line.split()
        if f[2] != 'exon' : continue
        beg = int(f[3])
        end = int(f[4])
        total += end - beg + 1
        exons += 1
        print(f[3], f[4])

print(total/exons)

k = 4
seq = 'CAGATTATTATTCAGAT'
for i in range(len(seq) -k + 1):
    kmer = seq[i : i + k]
    print(kmer)
    '''
for defline, seq in mcb185.read_fasta(filepath):
    print(defline, len(seq), seq[:20], '..', seq[-20:1]
    
