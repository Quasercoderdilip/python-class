# find the minimum number in array:

def min_num_arr(arr):
    if not arr:
        return None;

    num = arr[0];

    for i in arr:
        if num > i:
            num = i;


    return num;

in_arr = [4, 2, 8, 5, 1, 0, 90, 2];

print(min_num_arr(in_arr));
