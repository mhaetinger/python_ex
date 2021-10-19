import math
print('=====EXERCÍCIO 18=====')
n = float(input('Digite o ângulo que você deseja: '))
se = math.sin(math.radians(n))
co = math.cos(math.radians(n))
tan = math.tan(math.radians(n))
print('O SENO do ângulo {:.1f}° é igual a {:.2f}'.format(n, se))
print('O COSSENO do ângulo {:.1f}° é igual a {:.2f}'.format(n, co))
print('A TANGENTE do ângulo {:.1f} [e igual a {:.2f}'.format(n, tan))
