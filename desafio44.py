print('{:=^40}'.format(' LOJAS GUANABARAS '))
preço = float(input('Preços das compras R$: '))
print('''FORMA DE PAGAMENTO
[ 1 ] dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual á opção?'))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra será parcela em {}x de R${:.2f} COM JUROS'.format(totalparc, parcela))
else:
    total = preço
    print('OPÇÃO INVALIDA DE PAGAMENTO!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
