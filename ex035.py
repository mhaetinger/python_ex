print('\033[30;44m=====EXERCÍCIO 35=====\033[m')
a = float(input('\033[1;97mInsert the first segment: '))
b = float(input('\033[1;97mInsert the second segment: '))
c = float(input('\033[1;97mInsert the third segment: '))
if a + b > c and b + c > a and a + c > b:
    print('\033[1;97mThis triangle \033[4;34mEXISTS!')
else:
    print('\033[1;97mThis triangle is \033[4;31mIMPOSSIBLE!')
