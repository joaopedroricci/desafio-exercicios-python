num = cont = soma = 0
num = int(input('Informe um número [ 999 para parar]:'))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Informe um número [ 999 para parar]:'))
print('Você digitou {} números e a soma de todos é {} '.format(cont, soma))

