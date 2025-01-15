# *Question: Find the Sum of Digits of a Number*
   

def sum_num(num):
    str_num = str(num);
    sum = 0 ;
    for i in str_num:
        j = int(i);
        sum += j

    return sum
    

n = int(input('Enter the number : '));
print(sum_num(n));
