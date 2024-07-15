carro = float(input('Qual a quantidade de Km rodados: '))
dias = int(input('Qual a quantidade de dias de aluguel?: '))
soma1 = carro * 0.15
soma2 = dias * 60
print('Você tera que pagar o valor equivalente a R${:.2f} ' .format(soma1 + soma2))
