import random
from random import randint

def GameWin():
    try:
        if comp==user:
            print("The game is tie")

        elif comp == 's':
            if user == 'r':
                print(f'{user_name} won')
            elif user == 'p':
                print(f'{user_name} lose')
        elif comp == 'p':
            if user == 's':
                print(f'{user_name} won')
            elif user == 'r':
                print(f'{user_name} lose')
        elif comp == 'r':
            if user == 'p':
                print(f'{user_name} won')
            elif user == 's':
                print(f'{user_name} lose')
        
    except Exception as e:
        print(e)


print("computer turn : paper(p), rock(r) and scissor(s)")
user_name = input('Enter your Name: ').capitalize()
randno =randint(1,3)
if randno==1:
    comp='r'
elif randno==2:
    comp='p'
elif randno==3:
    comp='s'
try:
    user = input('''Enter rock paper or scissor:\n''').lower()
    print(f'Computer entered: {comp}')
    GameWin()
except Exception as e :
    print("You entered a invalid input")





