print('=====EXERCÍCIO 29=====')
km = float(input('Insert your speed in KM/H: '))
print(f'Your speed is {km:.2f}KM/H')
if km >= 80.0:
    t = (km - 80) * 7
    print(f'You pass the speed limit, you need to pay ${t:.2f} for the traffic ticket')
else:
    print('You are driving well, keep going!')
