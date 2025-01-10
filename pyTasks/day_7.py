
storage = [];
done = 'no'
while done == 'no' :
    goal = str(input('enter your goal : '));
    storage.append(goal);
    done = str(input('Are you done ? (yes/no)')).strip();


def sorted_ans(get_val):

    len_arr = len(get_val)

    for i in range(len_arr):
        for j in range(0, len_arr - i - 1):

            if get_val[j] > get_val[i + 1] :

                get_val[j], get_val[j+1] = get_val[j+1], get_val[j]

    return get_val;


print(sorted_ans(storage));
