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


# reverse an array (Two pointer approach) :

arr = [1,2,3,4,5,6,67,6]

start, end = 0, len(arr) - 1

while start < end :
    arr[start], arr[end] = arr[end], arr[start]

    start += 1;
    print(start);

    end -= 1;
    print(end);


print(arr);