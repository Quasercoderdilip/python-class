#Strings : 


#slicing using indexing : 

# name = 'Dilip kumar';

# cut_mark = name.find(' ');

# print(name[:cut_mark]);


var = 'Hello world';

#print(var[4:-1]);

email = str(input('Enter your email : '));

user_name = (email[:email.index('@')]);
domain = (email[email.index('@'):]);

print(user_name);
print(domain);

print(f'your username is {user_name} and your domain is {domain}');