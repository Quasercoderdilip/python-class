import datetime

def check_period_hour(hour):
    if hour == 9 :
        print('(09:00 - 10:00) English period')
    elif hour == 10 :
        print('(10:00 - 11:00) Tamil period') 
    elif hour == 11 :
        print('(11:00 - 12:00) Maths period') 
    elif hour == 12 :
        print('(12:00 - 1:00) Lunch period') 
    elif hour == 1 :
        print('(01:00 - 02:00) Social period') 
    elif hour == 2 :
        print('(02:00 - 03:00) science period') 
    elif hour == 3 :
        print('(3:00 - 04:00) Gk period') 
    elif hour == 4 :
        print('(04:00 - 05:00) P.E.T period') 
    else:
        print('this is not a school timing')


h = int(input('enter hour : '));
m = int(input('enter minute : '));
s = int(input('enter seconds : '));

time = datetime.time(h, m, s);
print(time);

check_period_hour(h)
