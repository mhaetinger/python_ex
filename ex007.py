print('=====EXERCÍCIO 7=====')
m = float(input('Digite a nota em Matemática: '))
p = float(input('Digite a nota em Português: '))
c = float(input('Digite a nota em Ciência: '))
g = float(input('Digite a nota em Geografía: '))
md = (m + p + c + g) / 4
print('A média do aluno é {:.2f}'.format(md))
