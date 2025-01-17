# remove all occurences of a given charcter from a string:

# my approach : 
# def remove_occurences(txt):
#     txt = txt
#     n_txt = ''

#     for char in txt:
#         if txt.count(char) == 1:
#             n_txt += (char)

#     txt = n_txt

#     return txt


# print(remove_occurences(input('Enter string to remove occurences : ')))


def remove_occurences(txt):
    char_count = {}
   
    for char in txt:
        char_count[char] = char_count.get(char, 0) + 1

    n_txt = ''.join(char for char in txt if char_count[char] == 1)

    return n_txt


print(remove_occurences(input('Enter string to remove occurences : ')))