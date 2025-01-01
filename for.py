#for loop:

# txt = 'Hello iam Robot';
# ind = [];

# for i,char in enumerate(txt):
#     if(char == ' '):
#         ind.append(i);
#         continue;

# print(ind);


#sum of all nums:
# n = 10;
# sumof = 0;

# for i in range(1,n+1):
#     sumof += i;

# print(sumof);


#vowels finder:

# txt = str(input('Enter your text : '));
# vowels = ['a', 'e', 'i', 'o', 'u'];
# no_vowels = 0 ;

# for i,char in enumerate(txt):
#     if(char.lower() in vowels):
#         print(f'Vowel found at index ({i}) : {char}');
#         no_vowels +=1;
#         continue;

# print(f'No of vowels : {no_vowels}');


#Multiplication tables : 


# table_num = int(input('Enter which table do you want :' ));
# n = int(input('And Enter how many times do you want :' ));
# print('\n')
# print(f'Tables of {table_num} : ')
# for i in range(1,n + 1) : 
#     print(f'{table_num} x {i} = {i * table_num}');



#reverse the list:

# n = ['a', 'e', 'i', 'o', 'u'];

# for i in n[::-1] :
#     print(i);

#reversing name : 

# name = str(input('Enter your name : ')) ;
# rev_name = '';

# for char in name[::-1] :
#     rev_name += char;

# print(f'Reversed name : {rev_name}');


# nested loops :
