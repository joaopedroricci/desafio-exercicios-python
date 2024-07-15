numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
while True:
    pessoa = int(input('Informe um número entre 0 e 20: '))
    while pessoa not in numeros:
        pessoa = int(input('Tente novamente, digite um número entre 0 e 20: '))
    if pessoa == numeros[0]:
        print('Você digitou o número Zero.')

    elif pessoa == numeros[1]:
        print('Você digitou o número Um.')

    elif pessoa == numeros[2]:
        print('Você digitou o número Dois.')

    elif pessoa == numeros[3]:
        print('Você digitou o número Três.')

    elif pessoa == numeros[4]:
        print('Vecê digitou o número Quatro.')

    elif pessoa == numeros[5]:
        print('Você digitou o número Cinco.')

    elif pessoa == numeros[6]:
        print('Você digitou o número Seis.')

    elif pessoa == numeros[7]:
        print('Você digitou o número Sete.')

    elif pessoa == numeros[8]:
        print('Você digitou o número Oito.')

    elif pessoa == numeros[9]:
        print('Você digitou o número Nove.')

    elif pessoa == numeros[10]:
        print('você digitou o número Dez.')

    elif pessoa == numeros[11]:
        print('Você digitou o número Onze.')

    elif pessoa == numeros[12]:
        print('Você digitou o número Doze.')

    elif pessoa == numeros[13]:
        print('Você digitou o número Treze.')

    elif pessoa == numeros[14]:
        print('Você digitou o número Catorze.')

    elif pessoa == numeros[15]:
        print('Você digitou o número Quinze.')

    elif pessoa == numeros[16]:
        print('Você digitou o número Dezesseis. ')

    elif pessoa == numeros[17]:
        print('Você digitou o número Dezessete.')

    elif pessoa == numeros[18]:
        print('Você digitou o número Dezoito.')

    elif pessoa == numeros[19]:
        print('Você digitou o número Deznove.')

    elif pessoa == numeros[20]:
        print('você digitou o número Vinte.')

    res = ' '
    while res not in 'SN':
        res = str(input('Você quer continuar [S/N]: ')).strip().upper()
    if res == 'N':
        break
