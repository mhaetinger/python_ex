from datetime import date
print('\033[1;30;44m=====EXERCÍCIO 32=====\033[m')
year = int(input('Insert a year, 0 for actual year :'))
if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')
