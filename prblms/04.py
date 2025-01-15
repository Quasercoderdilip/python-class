n = int(input('Enter the num for n :'));
num = n-1;
f_num = n;

for i in range(1,n):
    f_num *= num;
    num-=1;   
    

print(f_num);