#looping : 


#while loop:

# password = ''

# while password != 'python123':
#     password = str(input('Enter your password : '));

# print("Access granted!");


#continue keyword: to skip the rest of the current iteration and move to the next iteration.

i = 0
while i < 6:
  i += 1;
  if i == 3:
    continue;# jump directly to the next iteration.
  print(i);