print('\033[1;30;44m=====EXERCÍCIO 34=====\033[m')
salary = float(input('\033[1mWhat is your salary? $ '))
if salary >= 1250.00:
    plus = (salary * 10/100) + salary
    print(f'\033[36mWith 10% increase your new salary will be \033[1;32m${plus:.2f}')
else:
    plus = (salary * 15/100) + salary
    print(f'\033[36mWith 15% increase your new salary will be \033[1;32m${plus:.2f}')
