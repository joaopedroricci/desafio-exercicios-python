n1 = float(input('Informe o total percorrido:'))
soma1 = n1 * 0.50
soma2 = n1 * 0.45
if n1 <= 200:
    print('Você deverá pagar um total de: R${:.2f}'.format(soma1))
else:
    print('Sua distância é meior,você pagará um total de:R${:.2f} '.format(soma2))
