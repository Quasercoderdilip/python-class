# *Question: Find the GCD of Two Numbers*

# def GCD_finder(num_1, num_2):

#     d = list(range(1, 100 + 1))
#     t_d = []

#     for i in d:
#         if num_1 % i == 0 and num_2 % i == 0:
#             t_d.append(i)

#     return max(t_d)


# print(GCD_finder(int(input('Enter num_1 : ')),int(input('Enter num_2 : '))))





# Euclidean Algorithm

def GCD_finder(num_1, num_2):
    while num_2 != 0:
        num_1, num_2 = num_2, num_1 % num_2
    return num_1

print(GCD_finder(int(input('Enter num_1 : ')), int(input('Enter num_2 : '))))

