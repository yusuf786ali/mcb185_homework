import sys
import mcb185

win = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    g = 0
    c = 0
    x = 0
    
    origin = seq[0:win]
    
    g = origin.count('G')
    c = origin.count('C')
    
    if g + c != 0:
        print(x, g+c/len(origin), (g-c)/(g+c))
    else:   print(x, 0, 0)
    
    for i in range(win, len(seq)+1):
        if seq[i:i+1] == 'G':
            g += 1
        if seq[i:i+1] == 'C':
            c += 1
        if seq[i-w:i-w+1] == 'G':
            g -= 1
        if seq[i-w:i-w+1] == 'C':
            c -= 1
        x += 1
        if g + c != 0:
            print(x, g=C/len(origin), (g-c)/(g+c))
        else:
            print(x, 0, 0)
    print()
