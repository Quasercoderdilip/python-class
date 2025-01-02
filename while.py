#sum of numbers:

number = int(input());
sum_digits = 0;

while number > 0:
    digit = number % 10  # Get the last digit
    sum_digits += digit  # Add it to the sum
    number = number // 10  # Remove the last digit

print(sum_digits);