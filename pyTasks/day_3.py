# std_name = str(input('Enter your name : '));

# sub_1 = int(input('Enter your sub_1 mark/100 : '));
# sub_2 = int(input('Enter your sub_2 mark/100 : '));
# sub_3 = int(input('Enter your sub_3 mark/100 : '));
# sub_4 = int(input('Enter your sub_4 mark/100 : '));
# sub_5 = int(input('Enter your sub_5 mark/100 : '));

# if sub_1 or sub_2 or sub_3 or sub_4 or sub_5 > 100 and sub_1 or sub_2 or sub_3 or sub_4 or sub_5 < 0 :
#     print('Invalid marks.');
#     print('Marks is only out of 100.')
# else : 
#     total = sub_1 + sub_2 + sub_3 + sub_4 + sub_5 ;
#     tot_percent = total/5;

#     print(f'Student name : {std_name}');
#     print(f'Student name : {total}');
#     print(f'Student name : {tot_percent}%');


std_name = input('Enter your name: ')
marks = [int(input(f'Enter mark for subject {i+1}/100: ')) for i in range(5)]

if any(mark > 100 or mark < 0 for mark in marks):
    print('Invalid marks. Marks should be between 0 and 100.')
else:
    total = sum(marks)
    tot_percent = total / 5
    print(f'Student name: {std_name}')
    print(f'Total marks: {total}')
    print(f'Percentage: {tot_percent}%')
