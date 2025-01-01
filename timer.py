#countdown timer : 

import time;#time module.




time_in = int(input('Enter time in seconds : '));

for i in range(time_in + 1):
    time_in -= 1;
    print(i);
    time.sleep(1);

print('count is over');