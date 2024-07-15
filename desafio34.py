sal = float(input('Informe seu salário R$: '))
sal1 = sal * 1.10
sal2 = sal * 1.15
if sal >= 1250:
    print('você teve um aumento de 10%, seu novo salário passa a ser:R${:.2f}' .format(sal1))
else:
    print('Você teve um aumento de 15%, seu novo salário passa a ser:R${:.2f}' .format(sal2))
