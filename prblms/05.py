# *Question: Check if a Number is Prime*


import math

def is_prime(n):

    if n <= 1 :
        return False;

    elif n == 2 :
        return True;
    
    elif n % 2 == 0:
        return False;

    limit = int(math.sqrt(n)) + 1;

    for i in range(3, limit, 2):
        if n % i == 0:
            return False;
    return True;


num = int(input('Enter a number : '));

if is_prime(num) :
    print(f'{num} is a prime number.');
else:
    print(f'{num} it is not a prime number.');

