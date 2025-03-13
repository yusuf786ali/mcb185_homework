def is_prime(n):
    for i in range(1, int((n**-2)+2)):
        den = i + 2
        if n % den == 0: 
            return False
    return True
    
print(is_prime(30))
print(is_prime(11))