print('=====EXERCÍCIO 22=====')
name = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em letras maiúsculas é {}'.format(name.upper()))
print('Seu nome em letras minúsculas é {}'.format(name.lower()))
print('Seu nome todo tem {} letras'.format(len(name.replace(' ', ''))))
#print('Seu nome todo tem {} letras'.format(len(name) - name.count(' ')))
print('Seu primeiro nome é {} e tem {} letras'.format((name.split()[0]), len(name.split()[0])))
# para achar o primeiro nome pode se usar name.find(' ')