
num_starter = 1;
num_limit = 100;
except_nums = [];

for i in range(num_starter,num_limit + 1):
    if i == 77 or i == 86 or i == 32 :
        except_nums.append(i)
        continue;
    else:
        print(i);


print(except_nums);