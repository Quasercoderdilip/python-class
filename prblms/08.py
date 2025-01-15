# *Question: Fibonacci Series up to N Terms*:

n = int(input('Enter the number to input : '));
a,b = 0,1
for _ in range(n):
    print(a);
    a,b = b, a+b;
    