from random import randint
from time import sleep
print('\033[1;30;44m===================EXERCÍCIO 28====================\033[m')
print('-=-' * 20)
print('\033[7;97;40mI WILL THING IN A NUMBER FROM 0 TO 5, TRY TO GUESS...\033[m')
print('-=-' * 20)
r = randint(0, 5)
num = int(input('\033[1;97mWhat was the number?\033[m'))
print('\033[1;34mProcessing the number...\033[m')
sleep(1)
if num == r:
    print(f'\033[1;32mYOU WIN!\033[1;97m The chosen number was {r}')
else:
    print(f'\033[1;31mYOU LOST THE GAME!\033[1;97m The chosen number was {r} and not {num}')
