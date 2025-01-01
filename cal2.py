#compound intrest calculator : 

principle = 0;
rate = 0;
time = 0;

while True :
    principle = float(input('Enter your principle amount : '));
    if principle < 0 :
        print('Priciple amount cannot be negative.');
    else :
        break;

while True :
    rate = float(input('Enter your rate of intrest : '))
    if rate < 0 :
        print('Rate of intrest cannot be negative.');
    else :
        break;

while True :
    time = float(input('Enter your time : '))
    if time < 0 :
        print('Time of intrest cannot be negative.');
    else :
        break;

