carro = int(input('Informe a velocidade do carro: '))
soma1 = (carro - 80)*7
if carro <= 80:
    print('VELOCIDADE PERMITIDA!')
else:
    print('MULTADO!')
    print('você deverá pagar uma multa equivalente a: {}' .format(soma1))
