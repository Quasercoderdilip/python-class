# *Question: Fibonacci Series up to N Terms*:

n = int(input('Enter the number to input : '));
a,b = 0,1
fib_series = []

for _ in range(n):
    fib_series.append(a)
    a, b = b, a + b

print(fib_series)

