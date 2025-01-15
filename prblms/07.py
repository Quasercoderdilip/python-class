# *Question: Count Number of Digits in a Number*

user_num = int(input('Enter the number : '));

def find_digits(in_num):
    num = str(in_num);
    digits = len(num);
    return digits;

print(find_digits(user_num));

