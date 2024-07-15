ano = int(input('Informe um ano:'))
ano1 = ano % 4
ano2 = ano % 100
ano3 = ano % 400
if (ano1 == 0 and ano2 != 0) or (ano3 == 0):
    print('Esse Ano é Bissexto!')
else:
    print('Esse Ano Não é Bissexto!')
