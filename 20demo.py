import math
import random
#tuple
t = 1, 2 #this is a tuple
print(t)
print(type(t))

p = 'hi'
print(p)

person = 'Steve', 21, 57891.50
print(person)

def midpoint(x1, y1, x2, y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) /2
    return x, y

print(midpoint(1, 2, 3, 4))
m = midpoint(1, 2 , 3, 4)
mx, my = midpoint(1, 2, 3, 4)
print(mx, my)
print(m[0], m[1])
'''
while True:
    print('hello')
'''
i = 0
while True:
    i = i + 1
    print('hey', i)
    if i == 3: 
        break
    
i = 0
while i < 3:
    i = i + 1
    print('hey', i)

i = 1
while i < 10:
    print(i)
    i = i + 3
print('final value of i is', i)

for i in range(1, 10, 3):
    print(i)

for i in range(0, 5):
    print(i)

for i in range(5):
    print(i)

for i in range(3, -1, -1): print(i)

basket = 'milk', 'eggs', 'bread'

for thing in basket:
    print(thing)
    
for i in range(len(basket)):
    print(basket[i])
    
for i in range(7):
    if i % 2 == 0: print(i, 'is even')
    else:          print(i, 'is odd')
    
for i in range (1, 101):
    if i % 15 == 0:    print('FizzBuzz')
    elif i % 5 == 0:   print('Buzz')
    elif i % 3 == 0:  print('Fizz')
    else:              print(i)

def triangle(number):
    total = 0
    for i in range(number + 1):
        total = total + i
    return total

print(triangle(6))

def factorial(number):
    total = 1
    if number == 0: return 1
    for i in range(number, 0, -1):
        total = total * i
    return total

print(factorial(6))
print(factorial(0))

def poisson(n, k):
    for i in range(n, k):
        total = (math.pow(n, k) * math.pow(math.e, -n) / factorial(k))
    return total

print(poisson(4, 10))

def nchoosek(n, k):
    total = factorial(n) / factorial(k) * factorial(n - k)
    return total

print(nchoosek(4, 10))

def euler(end):
    total = 0
    for n in range(end):
        total = total + (1 / factorial(n))
    return total

print(euler(1000))

def prime(n):
    if n < 2: return False
    for i in range(2, 100):
        if n % i == 0: return False
    return True

print(prime(120))

def is_prime(n):
    for den in range(2, n//2 + 1):
        if n % den == 0: return False
    return True
    
print(is_prime(11))

def peye(end):
    total = 3
    sign = 1
    for n in range(2, end, 2):
        total = total + 4/(n * (n + 1) * (n + 2))*sign
        sign = sign * -1
        print(total)
    return total
print(peye(200))

for i in range(5):
    print(random.random())

for i in range(3):
    print(random.randint(1,6))

random.seed(1)
print(random.random())
print(random.random())
random.seed(2)
print(random.random())
print(random.random())
random.seed(1)
print(random.random())
print(random.random())

