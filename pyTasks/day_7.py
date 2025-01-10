
storage = [];
done = 'no'
while done == 'no' :
    goal = str(input('enter your goal : '));
    storage.append(goal);
    done = str(input('Are you done ? (yes/no)')).strip();


print(sorted(storage));



# for i in storage:
#     print(sorted());