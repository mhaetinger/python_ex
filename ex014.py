print('=====EXERCÍCIO 14=====')
grau = float(input('Digite temperatura atual em °C: '))
faren = grau * 9 / 5 + 32
kelvin = grau + 273.15
print('Se convertermos {}°C, para fahrenheit temos {:.1f}°F e para kelvin teriamos {:.1f}K'.format(grau, faren, kelvin))
