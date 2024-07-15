numeros = list()
while True:
    valor = int(input('Informe um valor: '))
    if valor not in numeros:
        numeros.append(valor)
        print('Valor Adicionado com sucesso!')
    else:
        print('Valor duplicado! não vou adicionar...')
    res = ' '
    while res not in 'SN':
        res = str(input('você quer continuar: [S/N]: ')).strip().upper()[0]
    if res == 'N':
        break
print(f'Os valores adicionados foram: {numeros}')