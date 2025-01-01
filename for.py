#for loop:

txt = 'Hello iam Robot';
ind = [];

for i,char in enumerate(txt):
    if(char == ' '):
        ind.append(i);
        continue;

print(ind);
