peso = float(input('\033[31mInforme seu peso\033[m: '))
altura = float(input('\033[31mInforme sua altura\033[m: '))
imc = (peso) / (altura ** 2)
if imc < 18.5:
    print('\033[34mABAIXO DO PESO\033[m')
    print(imc)
elif imc <= 18.5 < 25:
    print('\033[34mPESO IDEAL\033[m')
    print('Seu imc: {:.2f}'.format(imc))
elif imc <= 25 < 30:
    print('\033[34mSOBREPESO\033[m')
    print('Seu imc: {:.2f}'.format(imc))
elif imc <= 30 < 40:
    print('\033[34mOBESIDADE\033[m')
    print('Seu imc: {:.2f}'.format(imc))
elif imc >= 40:
    print('\033[34mOBESIDADE MÓRBIDA\033[m')
    print('Seu imc: {:.2f}'.format(imc))