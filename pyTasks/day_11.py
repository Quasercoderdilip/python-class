import random


def Num_game(times):
    
    score = 0

    for i in range(1, times + 1):
        print(f'Round {i}')
        rand_num = random.randint(1,10)
        in_num = int(input('Enter number as your guess (1-10) : '))
        print(f'Number to win : {rand_num}')

        if in_num == rand_num :
            print('Win')
            score += 1
        else : 
            print('Lose')
            # if score > 0:
            #     score -= 1
            # else :
            #     score += 0
        print(f'Score : {score}')
        print()
        


Num_game(int(input('Enter how many rounds you have like to play : ')))

