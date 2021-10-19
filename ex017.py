import math

print('=====EXERCÍCIO 17=====')
opo = float(input('Digite o a medida do cateto oposto: '))
ad = float(input('Digite a medida do cateto adjacente: '))
hypo = math.hypot(opo, ad)
print('O valor da hipotenusa é {:.2f}'.format(hypo))
