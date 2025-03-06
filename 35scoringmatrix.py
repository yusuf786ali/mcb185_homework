import sys

nucleotides = (sys.argv[1])
match = (sys.argv[2])
mis = (sys.argv[3])

print("  ", end="")
for nucT in nucleotides:
    print(f' {nucT}', end=' ')
print()
for nucS in nucleotides:
    print(nucS, end=' ' )
    for nucT in nucleotides:
        if nucT == nucS:
            print(f'{match} ', end= '')
        else:
            print(f'{mis}', end = '')
    print()
    