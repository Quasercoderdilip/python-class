
# for i in range(1,101):
#     if i == 77 or i == 86 or i == 32 :
#         continue;
#     else:
#         print(i);

#another approach:
print(*(i for i in range(1, 101) if i not in {77, 86, 32}))
