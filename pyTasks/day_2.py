
letters = ['a','b','c'];

# for i in letters:
#     for j in letters:
#         if i != j:
#             print(i+j);



#another approach:
combinations = [ i+j for i in letters for j in letters if i != j ];
print(combinations);