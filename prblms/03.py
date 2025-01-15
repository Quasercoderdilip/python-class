#*Question: Reverse an Array*


arr = ['apple','banana','orange'];
reversed_arr = [];
max_ind = len(arr)-1

for item in arr:
    if max_ind >=0 :
        reversed_arr.append(arr[max_ind]);
        max_ind -= 1;
    else:
        break;

print(reversed_arr);

