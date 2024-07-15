numeros = list()
total = 0
while True:
    valor = int(input('Informe um valor: '))
    total += 1
    if valor not in numeros:
        numeros.append(valor)
    res = ' '
    while res not in 'SN':
        res = str(input('Você quer continuar: [S/N]: ')).strip().upper()
    if res == 'N':
        break
print('-='*30)
print(f'No total foram digitados {total} números')
numeros.sort(reverse=True)
print(f'A lista em ordem decrescente: {numeros}')
if 5 in numeros:
    print('O número 5 está presente na lista.')
else:
    print('O número 5 não está presente na lista.')
