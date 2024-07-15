numero1 = int(input('\033[31mInforme o primeiro número\033[m: '))
numero2 = int(input('\033[31mInforme o segundo número\033[m: '))
if numero1 > numero2:
    print('\033[34mO primeiro valor é maior\033[m')
elif numero2 > numero1:
    print('\033[34mO segundo valor é maior\033[m')
elif numero1 == numero2:
    print('\033[34mOs dois valores são iguais\033[m')