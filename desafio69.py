tot18 = totH = totM20 = 0
print('-'*20)
print('CASDASTRO DE PESSOAS')
print('-'*20)
while True:
        idade = int(input('Idade: '))
        sexo = ' '
        while sexo not in 'MF':
                sexo = str(input('Sexo [M/F]: ')).strip().upper()
        if idade >= 18:
                tot18 += 1
        if sexo == 'M':
                totH += 1
        if sexo == 'F' and idade < 20:
                totM20 += 1
        res = ' '

        while res not in 'SN':
                res = str(input('Quer continuar [S/N]: ')).strip().upper()
        if res == 'N':
                break
print(f'Ao todo temos {tot18} pessoa maiores de 18.')
print(f'Ao todo temos {totH} homesn cadastrados.')
print(f'Ao todo temos {totM20} mulheres com menos de 20 anos.')
