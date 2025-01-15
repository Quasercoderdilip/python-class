# multiplications of number :

num = int(input('Enter the num for multiplies : '));
limit = int(input('Enter the max limit for multiplies : ')) + 1;


for i in range(1,limit):
    print(f'{num} x {i} = {num*i}'); 