print('=====EXERCÍCIO 8=====')
m = float(input('Digite o valor a ser convertido: '))
print('{} metros equivalem: \nA {:.2f} Km \n{:.2f} Hm \n{:.2f} Dam'.format(m, (m/1000), (m/100), (m/10)))
print('{:.0f} Dm \n{:.0f} centímetros \n{:.0f} milímetros'.format((m*10), (m * 100), (m * 1000)))
