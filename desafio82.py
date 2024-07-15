numeros = list()
par = list()
impar = list()
while True:
    valor = int(input('Informe um valor: '))
    if valor not in numeros:
        numeros.append(valor)
    res = ' '
    while res not in 'SN':
        res = str(input('Você quer continuar [S/N]')).strip().upper()
    if res == 'N':
        break
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
print(f'Primeira lista: {numeros}')
print(f'Lista de numeros Pares: {par}')
print(f'Lista de valores Ímpares: {impar}')
