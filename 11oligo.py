def tm(a, c, g, t):
    nt = a + c + g + t
    if nt <= 13: print((a + t*2)+ (g + c)*4)
    else:        print(64.9 + (41*(g + c - 16.4)) / (a + t + g + c))

tm(1, 1, 3, 4)
