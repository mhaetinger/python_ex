print('=====EXERCÍCIO 31=====')
km = float(input('Insert how long is your trip in KM: '))
if km <= 200:
    p = km * 0.50
    print(f'Because your trip limite is inside 200km the price will be ${p:.2f}')
else:
    p = km * 0.45
    print(f'Because your trip run through 200km the price will be ${p:.2f}')
