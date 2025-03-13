import sys
import mcb185


aas = [
    "I", "V", "L", "F", "C", "M", "A", "G", "T", "S", "W", "Y", "P", 
    "H", "E", "Q", "D", "N", "K", "R"]

prob = [
    4.5, 4.2, 3.8, 2.8, 2.5, 1.9, 1.8, -0.4, -0.7, -0.8, -0.9, -1.3, 
    -1.6, -3.2, -3.5, -3.5, -3.5, -3.5, -3.9, -4.5]


def kd(seq):
    total = 0
    for nt in seq:
        if nt in aas:
            toalt += prob[let.index(nt)]
    return total / len(seq)


total_count = 0
for defline, seq in mcb185.read_fasta(sys.argv[1]):

    signal = False
    trans = False

    Nterm = seq[0:30]
    Cterm = seq[30:]

    for i in range(0, len(Nterm)-8+1, 1):
        if kd(Nterm[i:i+8]) >= 2.5:
            signal = True

    for i in range(0, len(Cterm)-11+1, 1):
        if kd(Cterm[i:i+11]) >= 2.0:
            trans = True 

    if signal == True and trans == True:
        print(defline)
        total_count += 1
                        
print(total_count)