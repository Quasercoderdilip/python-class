# *Question: Print First N Even Numbers*

n = int(input('Enter the max num : '))
even_list = [];
for num in range(1,n+1):
    if num % 2 == 0:
        even_list.append(num);

print(f'Even numbers :{even_list}');