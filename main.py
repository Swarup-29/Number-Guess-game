import random

def User_input():
    num_to_guess = random.randint(1,100)
    attampts = 0
    print("Welcome to Number Guess game")
    print("i am thinking about 1 to 100 in between one number..")

    while True:
        User_guess = int(input('Enter your guess : '))
        attampts += 1

        if User_guess < num_to_guess:
            print("To low,,,Try again..")
        elif User_guess > num_to_guess:
            print('To high,,,Try again..')
        else:
            print(f'Correct🤩!!!,,...you win and you you take attampt to guess is {attampts}')
            break
    

User_input()