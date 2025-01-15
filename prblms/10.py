# remove duplicates from an array : 

def arr_cleaner(arr):

    cleaned_arr = [];

    for i in arr:
        if i in cleaned_arr:
            continue;
        else:
            cleaned_arr.append(i);

    arr = cleaned_arr;
    return arr;

in_arr = [1,2,3,4,5,6,1,2,3,4,5,6];

in_arr = arr_cleaner(in_arr);

print(in_arr);


