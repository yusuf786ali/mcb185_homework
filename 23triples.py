import math
n = 100
for a in range(1, n):
    for b in range(1, n):
        c = math.sqrt(a**2 + b**2)
        if c % 1 == 0:
            print(a, b, c, 'pythagorean triple')