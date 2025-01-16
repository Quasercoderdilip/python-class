# *Question: Count Vowels in a String*


def vowel_counter(para):
    v = ['a','e','i','o','u'];
    count = 0 ;
    cl_para = para.replace(' ', '').replace('.', '').replace(',','');
    for i in cl_para:
        print(i)
        for j in v:
            if i == j :
                count += 1;
    return count;


p = 'Your code works correctly for calculating the power of a number. However, there are a few improvements that can make it more robust and easier to read. Let me first explain how your code';


print(vowel_counter(p))
