casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento: '))
prestação = casa / (anos * 12)
minimo = salário * 30 / 100
print('Para pagar um casa de {:.2f} em anos {}'.format(casa, anos, end=''))
print('a prestação será de {:.2f}'.format(prestação))
if prestação <= minimo:
    print('impréstimo pode ser concedido')
else:
    print('Impréstimo negado')


