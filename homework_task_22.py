import random

print('What is number?')
print('_______________')

def greeting():
    print()
    print()
    print('Try to guess, what is the number?')
    print('---------')
    print('Or push <<q>> to leave.')

def who_is_winner(user_number, computer_number):
    result = True
    if user_number == computer_number:
        result = True
    if not user_number == computer_number:
        result = False
    return result

def game():
    print('Howdy folk!')

    while True:
        greeting()
        user_number = input()

        if user_number == 'q':
            print('Alright bye! Newer come back again ))))')
            break


        valid_choise = user_number.isnumeric() and 1 <= int(user_number) <= 10

        if not valid_choise:
            print("Enter valid data! It's 1, 2... 10 and no more, you silly pancake )))))")
            continue


        user_number = int(user_number)
        computer_number = random.randint(1,10)
        user_winner = who_is_winner(user_number, computer_number)
        if user_winner:
            print('%d? You damn right! Wanna go again?' % (user_number))
        if user_number > computer_number:
            print('Ha! Lol no! Not even close! Your number is too big')
        if user_number < computer_number:
            print('A-a-and you failed! Try better next time! Your number is too small')

game()