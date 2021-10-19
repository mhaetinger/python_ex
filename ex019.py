import random
print('=====EXERCÍCIO 19=====')
a1 = (input('Nome do primeiro aluno: '))
a2 = (input('Nome do segundo aluno: '))
a3 = (input('Nome do terceiro aluno: '))
a4 = (input('Nome do quarto aluno: '))
list = [a1, a2, a3, a4]
r = random.choice(list)
print('O aluno sorteado foi {}'.format(r))
