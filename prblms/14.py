# *Question: Count Vowels in a String*


def vowel_counter(para):
    v, count, cl_para = 'aeiou', 0, para.lower();
    
    for char in cl_para:
        if char in v:
            count += 1;
    return count;
    

p = 'Your code works correctly for calculating the power of a number. However, there are a few improvements that can make it more robust and easier to read. Let me first explain how your code';


print(vowel_counter(p))
