num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converte para BINÁRIO
[ 2 ] converte para OCTAL
[ 3 ] converte para HEXADECIMAL''')
opcão = int(input('sua opcão: '))
if opcão == 1:
    print('{} convertido para BINÁRIO é igual a: {}'.format(num, bin(num)[2:]))
elif opcão == 2:
    print('{} convertido para OCTAL é igual a: {}'.format(num, oct(num)[2:]))
elif opcão == 3:
    print('{} convertido para HEXADECIMAL é igual a: {}'.format(num, hex(num)[2:]))
else:
    print('opcão inválida. Tente novamente')
