from time import sleep
print('-'*20)
print('ESTATÍSTICAS DE PRODUTOS')
print('-'*20)
gasto = maiorM = menor = cont = 0
barato = ' '
while True:
    nomePro = str(input('Nome do produto: '))
    preco = float(input('Preço produto R$: '))
    cont += 1
    gasto += preco
    res = ' '
    if preco > 1000:
        maiorM += 1
    if cont == 1 or preco < menor:
        menor = preco
        batato = nomePro
    while res not in 'SN':
        res = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if res == 'N':
        break
print('Processando...')
sleep(2)
print(f'O preço total das compras è R$:{gasto:.2f}')
print(f'Ao todo {maiorM} produtos possuem um preço acima de R$1000,00 reais.')
print(f'E o produto mais barato é uma {nomePro} e custa R$:{menor:.2f}')

