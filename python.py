var_1 = 'Dilip kumar';
# print(var_1);


name,age,address,ph_no = 'Dilip kumar',23,'chennai',9176564700;

print(name);
print(ph_no);

# type casting : 
mark = 78;
print("my mark is " + str(mark));
print(type(mark));

# user_input : 

# name_2 = input('Name : ');
# age_2 = float(input('Age : '));
# e_mail = str(input('e-mail_ID : '));
# phone = str(input('ph_no : '));

# print(name_2);
# print(age_2);
# print(e_mail);
# print(phone);
# print(-5 - 2);


# print(*[abs(-5 - i) for i in range(10)]);


naname_san = input('say yes/no : ');

if naname_san == 'yes': 
    print('he is exist');
elif naname_san == 'no':
  print("doesn't exist");
else:
   print('invalid input');