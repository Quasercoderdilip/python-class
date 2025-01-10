import datetime

# def check_period_hour(hour):
#     if hour == 9 :
#         print('(09:00 - 10:00) English period')
#     elif hour == 10 :
#         print('(10:00 - 11:00) Tamil period') 
#     elif hour == 11 :
#         print('(11:00 - 12:00) Maths period') 
#     elif hour == 12 :
#         print('(12:00 - 1:00) Lunch period') 
#     elif hour == 1 :
#         print('(01:00 - 02:00) Social period') 
#     elif hour == 2 :
#         print('(02:00 - 03:00) science period') 
#     elif hour == 3 :
#         print('(3:00 - 04:00) Gk period') 
#     elif hour == 4 :
#         print('(04:00 - 05:00) P.E.T period') 
#     else:
#         print('this is not a school timing')


# h = int(input('enter hour : '));
# m = int(input('enter minute : '));
# s = int(input('enter seconds : '));

# time = datetime.time(h, m, s);
# print(time);

# check_period_hour(h)





# Function to map hours to periods
def check_period_hour(hour):
    # Periods mapping
    periods = {
        9: '(09:00 - 10:00) English period',
        10: '(10:00 - 11:00) Tamil period',
        11: '(11:00 - 12:00) Maths period',
        12: '(12:00 - 1:00) Lunch period',
        1: '(01:00 - 02:00) Social period',
        2: '(02:00 - 03:00) Science period',
        3: '(03:00 - 04:00) GK period',
        4: '(04:00 - 05:00) P.E.T period'
    }
    
    # Convert 24-hour format to 12-hour format
    if hour >= 13:
        hour -= 12
    
    # Check and print the period
    if hour in periods:
        print(periods[hour])
    else:
        print('This is not a school timing.')

# Input hour, minute, and second
try:
    h = int(input('Enter hour (0-23): '))
    m = int(input('Enter minute (0-59): '))
    s = int(input('Enter seconds (0-59): '))
    
    # Validate the inputs
    if not (0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59):
        print("Invalid time entered. Please enter values in the correct range.")
    else:
        # Create and display time
        time = datetime.time(h, m, s)
        print(f"Entered time: {time}")
        
        # Check the period
        check_period_hour(h)
except ValueError:
    print("Invalid input. Please enter numeric values for time.")
