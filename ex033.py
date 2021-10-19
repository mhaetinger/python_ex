print('\033[1;30;44m=====EXERCÍCIO 33=====\033[m')
n1 = int(input('\033[1;97mInsert the first number: '))
n2 = int(input('\033[1;97mInsert the second number: '))
n3 = int(input('\033[1;97mInsert the third number: '))

if n1 > n2 and n1 > n3:
    if n2 > n3:
        print(f'The biggest is {n1} and the smallest is {n3}')
    else:
        print(f'The biggest is {n1} and the smallest is {n2}')
elif n2 > n1 and n2 > n3:
    if n1 > n3:
        print(f'The biggest is {n2} and the smallest is {n3}')
    else:
        print(f'The biggest is {n2} and the smallest is {n1}')
else:
    if n1 > n2:
        print(f'The biggest is {n3} and the smallest is {n2}')
    else:
        print(f'The biggest is {n3} and the smallest is {n1}')
