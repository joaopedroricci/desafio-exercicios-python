nome = str(input('Digite seu nome: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}' .format(nome.upper()))
print('Seu nome em minúsculas é {}' .format(nome.lower()))
print('seu nome tem no total {} letras' .format(len(nome)-nome.count(' ')))
#print('Seu primeiro nome tem {} letras' .format(nome.find(' ')))
separa = nome.split()
print('seu primeiro nome tem {} e ele tem {} letras' .format(separa[0], len(separa[0])))
