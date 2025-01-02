#functions :

# def callPerson(person):
#     print(f'{person} is on call ' );


# callPerson('Mani');


# def add(a,b):
#     return a + b; 
# def sub(a,b):
#     return a - b;
# def mul(a,b):
#     return a * b;
# def div(a,b):
#     return a / b;



# print(add(1,2));
# print(sub(1,2));
# print(mul(1,2));
# print(div(1,2));


num_in = int(input('Enter the input : '));

def check(num):
    if num > 0 :
        if num % 2 == 0:
            print('even');
        else:
            print('odd');
    else:
        print('zero or below zero is cant be checked');


check(num_in);