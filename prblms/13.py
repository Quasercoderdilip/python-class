# *Question: Calculate Power of a Number*

def find_power(base, exponent):
    ans = base;
    for i in range(1,exponent):
        ans *= base;
        
    return ans;

print(find_power(0,2));

