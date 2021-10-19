print('=====EXERCÍCIO 13=====')
s = float(input('Digite seu salário: '))
a = s + s * (15/100)
d = a - s
print('O seu salário de R${:.2f} com 15% de aumento ficou R${:.2f}, tendo um aumento de R${:.2f}'.format(s, a, d))
