n = str(input('Digite seu nome: '))
nome = n.split()
print('Muito prazer em te conhecer: {} ' .format(n))
print('Seu primeiro nome é: {}' .format(nome[0]))
print('Seu ultimo nome é: {}' .format(nome[len(nome)-1]))