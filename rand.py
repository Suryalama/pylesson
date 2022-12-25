import random
def rand(x):

    random_number=random.randint(1,x)
    print('random number:',random_number)
    guess=0
    while random_number!=guess:
        guess=int(input(f'Guess the number between 1 and {x}: '))
      
        if guess>random_number:
            print('Sorry! Try again. Too high.')
        elif guess<random_number:
            print('Sorry! Try again. Too low.')
    print('Yes! Congrats. You have guessed correctly.')
rand(10)