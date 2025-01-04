
friends = [];
done = 'add'
while done == 'add' :
    #get the friends input.
    friend = input("Enter your friend name: ");
    friends.append(friend);
    done = str(input('Enter if finished = "done"/ if notFinished = "add" : '));
if done == 'done' : 
    print(f'{','.join(friends)} we all are together and spread love.');
else :
    print('Invalid input');