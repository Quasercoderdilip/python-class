# *Question: Find All Divisors of a Number*

def divisors(num):
    div = []

    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            div.append(i)
            if i != num // i:
                div.append(num // i)
                
    return sorted(div)


print(divisors(int(input('Enter the number for get divisors : '))))


