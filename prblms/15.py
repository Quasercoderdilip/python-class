# *Question: Count Consonants in a String*
import string

def consonant_counter(para):
    v, count, total, v_count = 'aeiou', 0, 0, 0; 
    cl_para = para.translate(str.maketrans('', '', string.punctuation)).replace(' ', '').lower()
    
    #print(cl_para);

    for char in cl_para:
        total += 1;
        if char.isalpha() and char not in v :
            count += 1 
        elif char.isalpha() and char in v:
            v_count += 1;         
    
    print(f'consonant count : {count}');
    print(f'vowel count : {v_count}');
    print(f'total count : {total}')

    return count;

p = 'Hello.';

print(consonant_counter(p));