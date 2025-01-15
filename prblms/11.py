# *Question: Find Maximum Number in an Array*

def max_num_arr(arr):
    if not arr:
        return None;

    num = arr[0];

    for i in arr:
        if num < i:
            num = i;


    return num;

in_arr = [1, 4, 2, 8, 5, 90, 2, 34, 56];

print(max_num_arr(in_arr));
