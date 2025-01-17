# *Question: Rotate an Array by K Positions*
# *Expected Output*: For [1, 2, 3, 4, 5] rotated by 2, output should be [4, 5, 1, 2, 3].

def Right_rotater(arr, k):
    rotated_arr = arr[-k:] + arr[:-k]
    return rotated_arr

def Left_rotater(arr, k):
    rotated_arr = arr[k:] + arr[:k]
    return rotated_arr


arr_1 = [1,2,3,4,5]
print(Right_rotater(arr_1,int(input('k for right rotation = '))))
print(Left_rotater(arr_1,int(input('k for left rotation = '))))

