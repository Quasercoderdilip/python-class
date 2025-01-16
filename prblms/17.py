# *Question: Count Occurrences of a Character in a String*

txt = input('Enter message : ')
char = input('Enter character to check the count : ')

if char in txt:
    count = txt.count(char);
    print(count)
else:
    print(f'Given character {char} is not in Message')
