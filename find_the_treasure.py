from random import randint
import json
import os.path


def create_file():
    with open('num.txt', 'w+') as f:
        while True:
            for i in range(10):
                f.write(f'{str(i)*randint(1,20)}')
            f.write('TREASURE')
            for i in range(9, -1, -1):
                f.write(f'{str(i)*randint(1,20)}')
            return


def check_range(n, offset):
    with open('num.txt', 'r') as readfile:
        length = len(readfile.readline())
        readfile.seek(n)
        while True:
            user = abs(int(input('How many step? '))
                       ) if offset == '1' else -abs(int(input('How many step? ')))
            sum_of_steps = user + n
            if sum_of_steps <= length and sum_of_steps >= 0:
                return sum_of_steps
            print('your chosen step is out of range ')


def update_scoreboard(n, s):
    path = './scoreboard.txt'
    # check_file = os.path.isfile(path)
    if os.path.isfile(path):
        with open('scoreboard.txt', 'r+') as f:
            score = json.load(f)
        score.update({n: s})
        if len(score) < 3:
            with open('scoreboard.txt', 'w+') as sfile:
                json.dump(score, sfile)
        else:
            res = dict(
                sorted(score.items(), key=lambda x: x[1])[:3])
            with open('scoreboard.txt', 'w+') as sfile:
                json.dump(res, sfile)
    else:
        score = {n: s}
        with open('scoreboard.txt', 'w+') as sfile:
            json.dump(score, sfile)


def play():
    # list_scoreboard
    name = input('Please enter your name: ')
    count = 0
    game_on = True
    user_step = int(input('How many step? '))
    with open('num.txt', 'r') as r:
        steps = user_step
        user_choice = ''
        char = ''
        current_location = 0
        while game_on:
            count += 1
            for i in r.read(steps):
                char = i
            if char in 'TREASURE':
                print(f'you hit {char}')
                print(
                    f'well done, you found the treasure. It took you {count} moves to get it done.')
                update_scoreboard(name, count)
                game_on = False
            else:
                print(f'you hit {char}')
                print('Please try again')
                current_location = r.tell()
                while True:
                    user_choice = input(
                        'Where you want to move? [1- forward 2-backwards] ')
                    if user_choice == '1':
                        steps = check_range(
                            current_location, user_choice)
                        break
                    elif user_choice == '2':
                        steps = check_range(
                            current_location, user_choice)
                        break
                    else:
                        print(
                            'invalid move, [1- forward 2-backwards] ONLY!!!! ')
                r.seek(0)


create_file()
play()
