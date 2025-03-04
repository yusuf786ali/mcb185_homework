import random

def savethrow(number, advantage):
    print(number)
    if advantage == 'Noadv':
        roll = random.randint(1, 20)
        print(roll)
        if roll < number:
            print('YOU FAILED')
        else:
            print('SUCCESS')
    if advantage == 'advantage':
        roll1 = 0
        roll2 = 0
        roll1 = random.randint(1, 20)
        print(roll1)
        roll2 = random.randint(1, 20)
        print(roll2)
        if roll1 > roll2:
            if roll1 < number:
                print('YOU FAILED')
            else: 
                print('SUCCESS')
        if roll2 > roll1:
            if roll2 < number:
                print('YOU FAILED')
            else:
                print('SUCCESS')
    if advantage == 'disadvantage':
        roll1 = 0
        roll2 = 0
        roll1 = random.randint(1, 20)
        print(roll1)
        roll2 = random.randint(1, 20)
        print(roll2)
        if roll1 < roll2:
            if roll1 < number:
                print('YOU FAILED')
            else: 
                print('SUCCESS')
        if roll2 < roll1:
            if roll2 < number:
                print('YOU FAILED')
            else:
                print('SUCCESS')

savethrow(15, 'disadvantage')