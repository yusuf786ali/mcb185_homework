import math

def char_to_prob(x):
    y  = ord(x)
    q = y - 33
    p = pow(10, -q / 10)
    return print(round(p, ndigits=5))

def prob_to_char(E):

    #make the decimal into acutal quality score

    q = -10 * math.log10(E)
    Q = round(q)
    #quality score into ascii (chr)
    return print(chr(Q + 33))

char_to_prob('A')
prob_to_char(0.501)
