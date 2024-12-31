# naname_san = input('say yes/no : ');

# if naname_san == 'yes': 
#     print('he is exist');
# elif naname_san == 'no':
#   print("doesn't exist");
# else:
#    print('invalid input');



#1:
# in_num = int(input('say one number : '));

# if in_num > 0 :
#     print('positive number');
# elif in_num < 0 :
#     print('negative number');
# else:
#     print('zero');


#2:
# in_num = int(input('say one number : '));

# if in_num > 0 :
#     print('positive number');
#     if in_num % 2 == 0:
#         print('even number');
#     elif in_num % 2 != 0:
#         print('odd number');
#     else:
#         print('invalid input');

# elif in_num < 0 :
#     print('negative numbers are not acceptable');
# else:
#     print('zero');


#3:
mrk = int(input('say marks : '));

if mrk <= 100 and mrk >= 0 :
    if mrk >= 90 :
        print('A - grade');
    elif mrk >= 80 :
        print('B - grade');
    elif mrk >= 70 :
        print('C - grade');
    elif mrk >= 50 :
        print('D - grade');
    elif mrk < 50 and mrk >= 35 :
        print('just pass E - grade');
    else:
        print('fail de-grade');
else:
    print('Invalid input');