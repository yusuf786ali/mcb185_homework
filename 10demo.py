# 10demo.py by Yusuf Ali

import math

print('hello, again') # greeting

""""
this is a
multi line
comment
"""
#scientific notation test

print(1.5e-2)

#addition test

print(1+1)

#subtraction test

print(1-1)

#multiplication test

print(2*2)

#division test

print(1/2)

#exponentiation test

print(2**3) # 2 to the power of 3

#integer divide test

print(5//2)

#remainder test

print (5%2)

#precedence test

print(5*(2+1))

#absolute value

print(abs(2))

#Power of (x to the power of y)

print(pow(5,3))

#rounding

print(round(9.85767685, ndigits =3))

#round up

print(math.ceil(8.7))

#round down

print(math.floor(8.7))

#log in base e
print(math.log(2.3))

""""
#log in any base x = base

(math.log 3(3))
"""

#square root
print(math.sqrt(25))

"""
#power of x to y

math.pow(x,y)
"""
#factorial math.factorial(x)

#library constants

print(math.e)
print(math.pi)
print(math.inf/math.inf)
print(math.nan)

print(0.1*1)
print(0.1*3)

#hypotenous of a triangle

a = 3                      #side of triangle
b = 4                      #side of triangle
c = math.sqrt(a**2 + b**2) #hypotenous

print(c)

print(type(a), type(b), type(c))

print(type(a), type(b), type(c), sep=', ', end='!\n')

#functions

def pythagoras(a,b):
    c = math.sqrt(a**2 + b**2)
    return c

hyp = pythagoras(3,4)
print(hyp)

def pythagoras(a,b):
    return math.sqrt(a**2 + b**2)

print(pythagoras(3,4))

def pythagoras(a,b): return math.sqrt(a**2 + b**2)

#area of circle

def circle_area(r): return math.pi * r**2

#area of rectangle
def rectangle_area(w, h): return w * h

#area of triangle using rectangle function

def triangle_area(w, h): return rectangle_area(w, h) / 2

#temperature from F to celcius

def tempFtoC(F):
    return F - 32 * (5/9)

def tempCtoF(C):
    return C * (9/5) + 32

print(tempCtoF(60))

print(tempFtoC(60))

def mphtoK(mph):
    return mph * 1.609

print(mphtoK(80))

def arithmeticmean(a, b, c):
    return (a * b * c) / 3

def geometricmean(a, b, c):
    return math.sqrt(a * b * c)

def harmonicmean(a, b, c):
    return (2*a*b) / (a + b)

print(arithmeticmean(5,30,9))
print(geometricmean(5,30,9))
print(harmonicmean(5,30,9))

def distancegraph(a, b, c, d):
    return math.sqrt((b-a)**2) + ((d-a)**2)

#strings

s = 'hello world'
print(s, type(s))

#conditionals

a = 2
b = 2
if a == b:
    print('a equals b')

if a == b:
    print('a equals b')
    print(a, b)

if a == b:
    print('a equals b')
print(a, b)

def is_even(x):
    if x % 2 == 0: return True
    return False

print(is_even(2))
print(is_even(3))

c == a == b
print(c)
print(type(c))

#if elif else conditional

if a < b:
    print('a < b')
elif a > b:
    print('a > b')
else:
    print('a == b')

#neatness

if   a < b: print('a < b')
elif a > b: print('a > b')
else:       print('a == b')

if   a < b: print('a < b')
elif a <=b: print('a <= b')
elif a == b:print('this will never print!')

if a < b or a > b: print('all things being equal, a and b are not')

if a < b and a > b: print('you are living in a strange world')

if not False: print(True)

a = 0.3
b = 0.1 * 3

if a < b:   print('a < b')
elif a > b: print('a > b')
else:       print('a == b')

print(abs(a-b))
if abs(a-b) < 1e-9: print('close enough')

if math.isclose(a, b): print('close enough')

s1 = 'A'
s2 = 'B'
s3 = 'a'

#String compared on ASCII, A < B, a > B

if s1 < s2: print('A < B')
if s2 < s3: print('B < a')

a = '1'
s = 'G'
if a < s: print('a < s')

def silly(m, x, b):
    y = m * x + b
print(silly(2 , 3 , 4))
