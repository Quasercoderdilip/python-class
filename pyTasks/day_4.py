from datetime import datetime

crnt_hour = datetime.now().hour;

if 5 <= crnt_hour < 12:
    print('Good mrng');
elif 12 <= crnt_hour < 17:
    print('Good afternoon');
elif 17 <= crnt_hour < 20:
    print('Good evening.');
else:
    print('Good night');