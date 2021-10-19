print('\033[1;30;44m=====EXERCÍCIO 33=====\033[m')
a = int(input('\033[1mInsert the first number: '))
b = int(input('\033[1mInsert the second number: '))
c = int(input('\033[1mInsert the third number: '))
big = a
if b > a and b > c:
    big = b
if c > a and c > b:
    big = c
print(f'\033[1;34mThe biggest number is {big}')
minor = a
if b < a and b < c:
    minor = b
if c < a and c < b:
    minor = c
print(f'\033[1;31mThe smallest number is {minor}')
